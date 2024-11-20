from random import choice, randint
import helper.tobeornottobe as to
import helper.eval as ev
import helper.code_to_execute as code
import helper.image as img
import helper.basic_word_match_algorithm as bsc
import helper.get_bot_info as bot_info
import helper.downloadyt as yt
import helper.quiz as quiz
import helper.scanvirus as sv
import helper.haram as haram
import asyncio
import aiohttp
import matplotlib.pyplot as plt
import os
import discord
import datetime

from huggingface_hub import InferenceClient

HF_API_TOKEN = "silly"
model_name = "meta-llama/Llama-2-7b-chat-hf"  
inference_client = InferenceClient(token=HF_API_TOKEN)

DAFTAR_FILE_PATH = 'daftar_messages.txt'

chat_history = []

global_deactivated = False
deactivated_servers = {}

commands_info = {
    "help": {"enabled": True, "desc": "ikan"},
    "hello": {"enabled": True, "desc": "ikan"},
    "eval": {"enabled": True, "desc": "ikan"},
    "math": {"enabled": True, "desc": "ikan"},
    "latex": {"enabled": True, "desc": "ikan"},
    "image": {"enabled": True, "desc": "ikan"},
    "impersonate": {"enabled": True, "desc": "ikan"},
    "echo": {"enabled": True, "desc": "ikan"},
    "youtube": {"enabled": True, "desc": "ikan"},
    "papan": {"enabled": True, "desc": "ikan"},
    "daftar": {"enabled": True, "desc": "ikan"},
    "botinfo": {"enabled": True, "desc": "ikan"},
    "quiz": {"enabled": True, "desc": "ikan"},
}


eval_allowed_servers = {1265919042653392906, 531064852307902477} 
special_users = {257276875506712578}

async def get_response(user_input: str, message, bot) -> str:
    global global_deactivated
    global chat_history

    lowered: str = user_input.lower()
    code_special: str = user_input
    server_id = message.guild.id
    user_id = message.author.id

    if '<@727842349094535248>' in lowered:
        arg = lowered.replace('<@727842349094535248>', '', 1)
        args = arg.split()
        arg_normal = code_special.replace('<@727842349094535248>', '', 1)
        args_code = arg_normal.splitlines()
        args_normal = arg_normal.split()
        command = args[0].strip()
        
        if command == 'help':
            help_message = "Penggunaan: `@multilinear <arg> (tanpa kurung <>)`\n🟨: selalu aktif \n🟩:aktif \n🟥:tidak aktif\n"
            help_message += "**Commands / Args:**\n"

            is_globally_deactivated = global_deactivated
            is_server_deactivated = deactivated_servers.get(server_id, False)

            for cmd, info in commands_info.items():
                description = info["desc"]
                if cmd in ["help", "botinfo"]:
                    mark = '🟨'  
                elif is_globally_deactivated or is_server_deactivated:
                    mark = '🟥'  
                else:
                    mark = '🟩' if info["enabled"] else '🟥'

                help_message += f" - {mark}`{cmd}` : {description}\n"

            help_message += "\nGlobal Status:\n"
            help_message += f"Bot global: {'🟥 Tidak Aktif' if is_globally_deactivated else '🟩 Aktif'}\n"
            help_message += f"Bot server: {'🟥 Tidak Aktif' if is_server_deactivated else '🟩 Aktif'}\n"

            return help_message

        if command == 'botinfo':
            return await bot_info.get_bot_info()

        if user_id not in special_users:
            if global_deactivated:
                return "lagi mimir"
            if deactivated_servers.get(server_id, False):
                return "di sini aku sudah mati (untuk server ini ga aktif ya. tunggu dinyalain.)"
            if not commands_info.get(command, {}).get("enabled", False):
                return "command ini dinonaktifkan."
            
        if command == 'daftar':
            if len(args) < 2:
                return "`@multilinear daftar <message>`"

            # Get the current timestamp
            now = datetime.datetime.now()
            timestamp = now.strftime("%H:%M %d %b %Y")
            user_name = message.author.name
            user_message = " ".join(args[1:])

            # Format the message
            log_entry = f"{timestamp} {user_name}({user_id}) '`{user_message}`'\n"

            # Append the message to the file
            try:
                with open(DAFTAR_FILE_PATH, 'a') as file:
                    file.write(log_entry)
                return f"berhasil: {log_entry.strip()}"
            except Exception as e:
                return f"Failed to log message: {str(e)}"
        
        elif command == 'slot':
            return await haram.slot_machine()

        elif command == 'papan':
            try:
                with open(DAFTAR_FILE_PATH, 'r') as file:
                    messages = file.read()
                return messages if messages else "papan kosong."
            except Exception as e:
                return f"Failed to read logged messages: {str(e)}"
        
        elif command == 'tail':
            try:
                with open(DAFTAR_FILE_PATH, 'r') as file:
                    messages = file.readlines()

                if not messages:
                    return "papan kosong."

                messages.pop(0)

                with open(DAFTAR_FILE_PATH, 'w') as file:
                    file.writelines(messages)

                return "berasil taillist."
            except Exception as e:
                return f"Failed to remove message: {str(e)}"

        elif command == 'head':
            try:
                with open(DAFTAR_FILE_PATH, 'r') as file:
                    messages = file.readlines()

                if not messages:
                    return "papan kosong"

                messages.pop()

                with open(DAFTAR_FILE_PATH, 'w') as file:
                    file.writelines(messages)

                return "berhasil headlist."
            except Exception as e:
                return f"Failed to remove message: {str(e)}"

        elif command == 'removeall':
            try:
                with open(DAFTAR_FILE_PATH, 'w') as file:
                    file.truncate(0)  
                return "All messages have been removed."
            except Exception as e:
                return f"Failed to remove all messages: {str(e)}"

        elif command == 'remove':
            if len(args) < 2:
                return "`@multilinear remove <index>`"

            try:
                index = int(args[1]) - 1  
                with open(DAFTAR_FILE_PATH, 'r') as file:
                    messages = file.readlines()

                if len(messages) == 0:
                    return "papan kosong."

                if index < 0 or index >= len(messages):
                    return f"1 sampai {len(messages)}."

                messages.pop(index)

                with open(DAFTAR_FILE_PATH, 'w') as file:
                    file.writelines(messages)

                return f"berhasil {index + 1} diahpus."
            except Exception as e:
                return f"Failed to remove message: {str(e)}"
            
        elif args[0].strip() == 'latex':
            try:
                if len(args) < 2:
                    return "`@multilinear latex <expression>`"
                
                latex_expression = " ".join(args[1:]) 
                
                plt.figure(figsize=(4, 2), facecolor='black')
                plt.text(0.5, 0.5, f"${latex_expression}$", fontsize=24, ha='center', va='center', color='white')
                plt.axis('off')  
                
                image_path = 'latex_image.png'
                plt.savefig(image_path, bbox_inches='tight', pad_inches=0.1)
                plt.close()  
                
                await message.channel.send(file=discord.File(image_path))
                
                os.remove(image_path)
                
                return f"gambar dari eksperi {latex_expression}."
            except Exception as e:
                return f"```error\n{e}\n```"

        elif args[0].strip() == 'echo':
            a = args[1:]
            return ' '.join(a)
            
        elif args[0] == 'image':
            a = args[1:]
            return await img.handle_image_request(a)
        
        elif args[0].strip() == 'mimir':
            if message.author.id == 257276875506712578:
                global_deactivated = True
                return "mimir mode activated"
            else:
                return "No, silly :3"

        elif args[0].strip() == 'amimir':
            if message.author.id == 257276875506712578:
                global_deactivated = False
                return "mimir mode deactivated"
            else:
                return "No, silly :3"
    
        if args[0].strip() == 'deactivate':
            if message.author.id == 257276875506712578:
                deactivated_servers[server_id] = True
                return "di sini aku mati."
            else:
                return "no, silly :3"
        
        elif args[0].strip() == 'reactivate':
            if message.author.id == 257276875506712578:
                deactivated_servers[server_id] = False
                return "di sana aku berdiri."
            else:
                return "no, silly :3"

        elif command == 'quiz':
            return await quiz.run_quiz(message, bot)

        elif command == 'scan':
            return await sv.scan_attachment(message)

        elif args[0].strip() == 'hello':
            return f'hello'

        elif command == 'deactivate_command':
            if user_id in special_users:
                if len(args) < 2:
                    return "`@multilinear deactivate_command <command>`"
                target_command = args[1].strip()
                if target_command in commands_info:
                    commands_info[target_command]["enabled"] = False
                    return f"Command `{target_command}` dinonaktifkan. 🟥"
                else:
                    return "Command tidak ditemukan."

        elif command == 'activate_command':
            if user_id in special_users:
                if len(args) < 2:
                    return "`@multilinear activate_command <command>`"
                target_command = args[1].strip()
                if target_command in commands_info:
                    commands_info[target_command]["enabled"] = True
                    return f"Command `{target_command}` diaktifkan. 🟩"
                else:
                    return "Command tidak ditemukan."

  
        elif args[0].strip() == 'math':
            to_eval = args[1:]
            with_step = args[-1:]
            to_eval_with_step = args[1:-1]

            if with_step[0] == 'true':
                return ev.eval(to_eval_with_step, True)
            elif with_step[0] == 'false':
                return ev.eval(to_eval_with_step, False)
            else:
                return ev.eval(to_eval)
        
        elif args[0].strip() == 'eval':
            if server_id not in eval_allowed_servers:
                return "cuma bisa dipakai di beberapa server tertentu ya."
            
            code_to_execute = "\n".join(args_code[1:]).strip()

            confirmation_message = await message.channel.send(
                "Powered By Docker\nbut still, tolong jangan eksekusi yang aneh aneh\nada numpy, matplotlib, panda.\neksekusi kode? (waktu konfirmasi 5s `[yes/no]`)\n*might take a while to execute*"
            )

            def check(m):
                return m.author == message.author and m.content.lower() in ['yes', 'no'] and m.channel == message.channel

            try:
                response = await bot.wait_for('message', check=check, timeout=5.0)

                if response.content.lower() == 'yes':
                    # Await the result of the code execution
                    execution_result = await code.execute_code_block(code_to_execute)
                    return execution_result
                elif response.content.lower() == 'no':
                    return "kode tidak dieksekusi."
                else:
                    return "tidak ada jawaban dalam waktu 5 detik, kode tidak dieksekusi."

            except asyncio.TimeoutError:
                return "tidak ada jawaban dalam waktu 5 detik, kode tidak dieksekusi."

        
        elif args[0].strip() == 'impersonate':
            if len(args) < 2:
                return "`@multilinear impersonate @target @pesan`"
            
            mentioned_users = message.mentions
            
            if not mentioned_users:
                return "`@multilinear impersonate @target @pesan`"
            
            print(mentioned_users)
            target_user = mentioned_users[1]  
            impersonation_message = " ".join(args[2:])  

            avatar_url = target_user.avatar.url if target_user.avatar else None
            avatar_bytes = None
            
            if avatar_url:
                async with aiohttp.ClientSession() as session:
                    async with session.get(avatar_url) as response:
                        if response.status == 200:
                            avatar_bytes = await response.read()

            webhook_name = target_user.nick if target_user.nick else target_user.name

            webhook = await message.channel.create_webhook(
                name=webhook_name,  
                avatar=avatar_bytes
            )

            await webhook.send(impersonation_message)

            await webhook.delete()

        if args[0].strip() == 'youtube':
            if len(args) < 2:
                return "`@multilinear youtube <link>`"
            
            link = args_normal[1]
            requester = message.author.mention
            output_path = 'downloads'

            notification_msg = await message.channel.send(f"downloading `{link}` for {requester}...")
            
            video_file = await yt.download_youtube_video(link, output_path)

            if os.path.exists(video_file):  
                await message.channel.send(
                    content=f"requested by {requester}: `{link}`",
                    file=discord.File(video_file)
                )
                os.remove(video_file) 
                await notification_msg.edit(content=f"Successfully sent `{link}` for {requester}.")
            else:
                await message.channel.send(f"Failed to download video from {link}. Error: {video_file}")
                await notification_msg.edit(content=f"Failed to download `{link}` for {requester}.")


        else:
            valid_commands = list(commands_info.keys())
            suggested_command = bsc.suggest_word(command, valid_commands)
            return suggested_command
