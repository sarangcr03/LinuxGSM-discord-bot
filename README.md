# LinuxGSM discord bot with python
![alt text](https://github.com/sarangcr03/linuxgsm-discord-bot/blob/main/Valheim_logo.jpg?raw=true)

This is a python script for a discord bot to run alongside your LinuxGSM game server. 

## Setup

Log into your discord developer portal and create an application.

Create a new bot and copy the bot token.

Replace YOUR_DISCORD_BOT_TOKEN with your token, YOUR_DISCORD_USER_ID with your discord ID and add more users in nessesary.

***NOTE: You need to enable developer mode in the discord desktop app to see your discord ID***

```ruby
import discord
import subprocess

intents = discord.Intents.default()
intents.members = True
intents.messages = True
client = discord.Client(intents=intents)

# Discord Bot Token
TOKEN = 'YOUR_DISCORD_BOT_TOKEN'

# Server path and name
SERVER_PATH = '/path/to/server'
SERVER_NAME = 'YOUR_SERVER_NAME'

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

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    # List of user IDs to allow with comma seperating each user.
    allowed_user_ids = ['YOUR_DISCORD_USER_ID', 'OPTIONAL_DISCORD_USER']

    # Check if the author is allowed to use the bot
    if str(message.author.id) not in allowed_user_ids:
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


client.run(TOKEN)

```
Check if python is installed in your server with this command:
```
python3 --version
```
If not installed on debian or ubuntu:
```
sudo apt-get update
sudo apt-get install python3
```
If not installed on centos:
```
yum update -y
yum install -y python3
```

