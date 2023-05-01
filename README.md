# LinuxGSM discord bot with python
![alt text]()

This is a python script for a discord bot to run alongside your LinuxGSM game server. 

## Setup

Log into your discord developer portal and create an application.

Create a new bot and copy the bot token.

Replace YOUR_DISCORD_BOT_TOKEN with your token.

Replace YOUR_DISCORD_USER_ID with your discord ID and add more users if nessesary.

***NOTE: You need to enable developer mode in the discord desktop app to see your discord ID.***

Replace /path/to/server with your game server's directory path, which is usually /home/USER where USER represents your servers username.

Replace YOUR_SERVER_NAME with your LGSM game server name. 

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
Install PIP on debian or ubuntu:
```
apt install python3-pip
```
Install PIP on centos:
```
yum install epel-release 
yum install python3-pip
```
Install subprocess.run:
```
pip install subprocess.run
```
### Importing the script
#### Option 1

Download and import the script.py file to your server.

#### Option 2

Make a new file and edit:
```
sudo nano script.py
```
Copy and paste this script to the new file:

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
## Run the script in the background with nohup

Run the script in an ssh session and close the terminal after successfully running
```
nohup python3 script.py &
```
***NOTE: Make sure you are in the directory where the script is located and that you don't do anything else in that terminal after running the script.***

## Adding bot to discord server

To add the bot to your discord server, use the url generator in the discord developer portal and select the bot option and give it whatever permission you would like.

Paste the url in a new tab and add to server.

***NOTE: you cannot controll this bot through the server you just added it to, adding it to a server is just so you can directly message the bot.***

Click on the bot's profile and select send message.

These are the avaelable commands:
```
!check-update
!force-update
!validate
!backup
!start
!details
!stop
!restart
!update
!monitor
!test-alert
!update-lgsm
```

If you want to stop the script:
```
pkill -f script.py
```


