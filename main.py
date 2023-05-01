import discord
import subprocess
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.messages = True
client = discord.Client(intents=intents)

# Discord Bot Token
TOKEN = os.getenv('TOKEN')

# Server path and name
SERVER_PATH = os.getenv('SERVER_PATH')
SERVER_NAME = os.getenv('SERVER_NAME')

# Server command aliases
COMMANDS = {
    'check-update': 'check-update',
    'force-update': 'force-update',
    'validate': 'validate',
    'backup': 'backup',
    'start': 'start',
    'details': 'details',
    'stop': 'stop',
    'restart': 'restart',
    'update': 'update',
    'monitor': 'monitor',
    'test-alert': 'test-alert',
    'update-lgsm': 'update-lgsm',
}

def is_user_allowed(author_id):
    allowed_user_ids = os.getenv('ALLOWED_USER_IDS').split(',')
    return str(author_id) in allowed_user_ids

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if not is_user_allowed(message.author.id):
        return

    if message.author == client.user:
        return

    if message.content.startswith('!'):
        command = message.content[1:]
        if command in COMMANDS:
            full_command = f"./{SERVER_NAME} {COMMANDS[command]}"
            result = subprocess.run(full_command.split(), cwd=SERVER_PATH, stdout=subprocess.PIPE)
            output = result.stdout.decode()
            chunks = [output[i:i+1900] for i in range(0, len(output), 1900)]
            for chunk in chunks:
                await message.channel.send(f"```{chunk}```")


def main():
    client.run(TOKEN)

if __name__ == '__main__':
    main()
