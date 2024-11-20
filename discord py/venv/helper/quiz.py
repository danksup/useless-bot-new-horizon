# quiz_logic.py
import io
import contextlib
import random
import asyncio
from .problem_gen import *

async def wait_for_response(message, bot, timeout: int = 30):
    try:
        user_msg = await bot.wait_for(
            'message', 
            check=lambda msg: msg.author == message.author, 
            timeout=timeout
        )
        return user_msg.content.strip()
    except asyncio.TimeoutError:
        return "timeout error"

async def run_quiz(message, bot):
    problems = generate_problems()
    problem = random.choice(problems)
    code = problem["code"]

    await message.channel.send(f"Python code snippet:\n```python\n{code}\n```")

    f = io.StringIO()
    global_scope = globals()
    
    try:
        with contextlib.redirect_stdout(f):
            exec(problem["code"], global_scope)
        output = f.getvalue().strip()
    except Exception as e:
        await message.channel.send(f"Error: {str(e)}")
        return

    await message.channel.send("Tebak output:")
    user_answer = await wait_for_response(message, bot)

    if user_answer == "timeout error":
        await message.channel.send("Waktu habis.")
        return

    if user_answer == output:
        await message.channel.send("Benar!")
    else:
        await message.channel.send(f"Salah! Jawaban: {output}")
