# DGSbot | LinuxGSM-discord-bot 

DGSbot is a Discord bot that helps you manage your game servers. It allows you to run server commands directly from Discord, without the need to access the server console. 

## Requirements

To use DGSbot, you need the following:

- Python 3.6 or higher
- A Discord bot token
- Access to the server where your game server is hosted

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/sarangcr03/LinuxGSM-discord-bot.git
   ```
   
2. Install the package:

   ```
   pip install LinuxGSM-discord-bot/DGSbot-1.0.tar.gz
   ```

3. Run the setup script to set your environment variables:

   ```
   DGSbot-setup
   ```

   ***You will be prompted to enter your Discord bot token, game server path, game server name, and allowed discord user IDs.***

4. Start the bot:

   ```
   nohup DGSbot &
   ```

   ***This will start the bot in the background and detach it from the terminal. If you want to stop the bot later, you can use `pkill -f DGSbot`.***
   

## Usage

Once the bot is running, you can send the following commands to teh bot in Discord:

- `!check-update`: Check for available updates.
- `!force-update`: Force an update to the latest version.
- `!validate`: Validate the server files.
- `!backup`: Create a backup of the server.
- `!start`: Start the server.
- `!details`: Show server details.
- `!stop`: Stop the server.
- `!restart`: Restart the server.
- `!update`: Update the server.
- `!monitor`: Monitor the server status.
- `!test-alert`: Test the alert system.
- `!update-lgsm`: Update LGSM.

## Python code for the bot

### __main__.py
```ruby
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

```
### setup_script.py
```ruby
import os
import dotenv

def setup():
    dotenv_path = os.path.expanduser('~/.env')
    with open(dotenv_path, 'w') as f:
        f.write(f"TOKEN={input('Enter your Discord bot token: ')}\n")
        f.write(f"SERVER_PATH={input('Enter your server path: ')}\n")
        f.write(f"SERVER_NAME={input('Enter your server name: ')}\n")
        f.write(f"ALLOWED_USER_IDS={input('Enter your allowed user IDs: ')}\n")

if __name__ == '__main__':
    setup()

```
## Contributing

If you find a bug or have a suggestion, please open an issue on GitHub. Pull requests are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](https
