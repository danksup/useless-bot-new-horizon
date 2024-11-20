import subprocess
import os
import uuid
import asyncio
import logging
import shlex
import ast

#logging
logging.basicConfig(level=logging.DEBUG)


def contains_dangerous_code(code: str) -> bool:
    try:
        tree = ast.parse(code)
        detector = DangerousCodeDetector()
        detector.visit(tree)
        if detector.found_issues:
            for issue in detector.found_issues:
                logging.warning(issue)
            return True
    except SyntaxError as e:
        logging.error(f"Syntax error in the code: {e}")
        return True  # Treat syntax errors as unsafe
    return False

class DangerousCodeDetector(ast.NodeVisitor):
    DANGEROUS_FUNCTIONS = {"os.system", "os.popen", "subprocess.call", 
                           "subprocess.run", "subprocess.Popen", "os.exec", "os.fork"}
    DANGEROUS_IMPORTS = {"os", "subprocess", "shutil", "platform"}
    
    def __init__(self):
        self.found_issues = []

    def visit_Import(self, node):
        for alias in node.names:
            if alias.name in self.DANGEROUS_IMPORTS:
                self.found_issues.append(f"Importing module '{alias.name}' is not allowed.")
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        if node.module in self.DANGEROUS_IMPORTS:
            self.found_issues.append(f"Importing from module '{node.module}' is not allowed.")
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute) and node.func.attr in self.DANGEROUS_FUNCTIONS:
            self.found_issues.append(f"Usage of '{node.func.attr}' is not allowed.")
        elif isinstance(node.func, ast.Name) and node.func.id in self.DANGEROUS_FUNCTIONS:
            self.found_issues.append(f"Usage of '{node.func.id}' is not allowed.")
        self.generic_visit(node)



async def run_docker_command(command: list, timeout: int = 100) -> str:
    try:
        process = await asyncio.create_subprocess_exec(
            *command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=timeout)
        
        # log stdout stderr
        logging.debug(f"Command stdout: {stdout.decode()}")
        logging.error(f"Command stderr: {stderr.decode()}")
        
        if process.returncode == 0:
            return stdout.decode()
        else:
            return stderr.decode()
    except asyncio.TimeoutError:
        logging.error(f"Command timed out: {command}")
        process.kill()
        return "timeout error"
    except Exception as e:
        logging.error(f"Error while running command: {e}")
        return f"Error: {e}"

async def execute_code_block(code: str) -> str:
    if code.startswith("```py") and code.endswith("```"):
        code = code[5:-3].strip()
        
        if contains_dangerous_code(code):
            return "```error\nCode contains dangerous functions or imports and will not be executed.\n```"
    
        unique_id = str(uuid.uuid4())
        docker_image = f"python-sandbox-{unique_id}"
        docker_container = f"container-{unique_id}"

        script_path = "temp_script.py"
        try:
            with open(script_path, "w") as f:
                f.write(code)
            
            dockerfile_content = f"""\
            FROM python:3.9-slim
            WORKDIR /usr/src/app
            COPY temp_script.py .
            RUN pip install numpy pandas matplotlib
            RUN adduser --disabled-password --gecos '' appuser
            USER appuser
            CMD ["python", "temp_script.py"]
            """
            
            with open("Dockerfile", "w") as f:
                f.write(dockerfile_content)

            build_result = await run_docker_command(["docker", "build", "-t", docker_image, "."])
            if "error" in build_result:
                return f"```error\nDocker build failed:\n{build_result}\n```"

            run_result = await run_docker_command(                      #4gb ram                4cores          no internet
                ["docker", "run", "--rm", "--name", docker_container, "--memory", "4096m", "--cpus", "4.0", "--network", "none", docker_image],
                timeout=100  
            )

            if run_result:
                return f"```py\n{code}\n```\n\nOutput:\n```py\n{run_result}\n```"
            else:
                return f"```error\n{run_result}\n```"
        except Exception as e:
            logging.error(f"Execution failed: {str(e)}")
            return f"```error\n{str(e)}\n```"
        finally:
            try:
                subprocess.run(shlex.split(f"docker rmi -f {docker_image}"), capture_output=True)
                subprocess.run(shlex.split(f"docker stop {docker_container}"), capture_output=True)
            except Exception as e:
                logging.error(f"Failed to clean up Docker resources: {e}")
            
            if os.path.exists(script_path):
                os.remove(script_path)
            if os.path.exists("Dockerfile"):
                os.remove("Dockerfile")
    else:
        return "cuma bisa eksekusi python ya. jangan lupa diwrap pakai triple backtick ya."
