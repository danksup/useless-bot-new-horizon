from typing import Final
import os
from dotenv import load_dotenv
from discord import *
from responses import get_response

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

async def send_message(message: Message, response) -> None:
    if not response:
        print('(Message was empty)')
        return

    if isinstance(response, str):
        is_private = response[0] == '?'
        if is_private:
            response = response[1:]
    else:
        response = str(response)
        is_private = response[0] == '?'
        if is_private:
            response = response[1:]

    try:
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running')

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content  
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    
    response: str = await get_response(user_message, message, client)
    
    await send_message(message, response)

def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()
