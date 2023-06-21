import interactions
import os
from dotenv import load_dotenv
import subprocess
import re

load_dotenv()

bot = interactions.Client(token=os.getenv('TOKEN'))

# Server path and name
SERVER_PATH = os.getenv('SERVER_PATH')
SERVER_NAME = os.getenv('SERVER_NAME')

# Guild ID for slash commands
GUILD_ID = os.getenv('GUILD_ID')

# Server command aliases
COMMANDS = {
    'start': 'start',
    'restart': 'restart',
    'monitor': 'monitor',
    'test-alert': 'test-alert',
    'details': 'details',
    'postdetails': 'postdetails',
    'skeleton': 'skeleton',
    'update-lgsm': 'update-lgsm',
    'update': 'update',
    'check-update': 'check-update',
    'force-update': 'force-update',
    'validate': 'validate',
    'backup': 'backup',
    'console': 'console',
    'debug': 'debug',
    'mods-install': 'mods-install',
    'mods-remove': 'mods-remove',
    'mods-update': 'mods-update',
    'install': 'install',
    'auto-install': 'auto-install',
    'developer': 'developer',
    'stop': 'stop',
}

def is_user_allowed(author_id):
    allowed_user_ids = os.getenv('ALLOWED_USER_IDS').split(',')
    return str(author_id) in allowed_user_ids

def remove_color_codes(string):
    """Removes color codes from a string."""
    return re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])', '', string)

@bot.command(
    name="start",
    description="Start the server",
    scope=GUILD_ID
)
async def start_server(ctx: interactions.CommandContext):
    if not is_user_allowed(ctx.author.id):
        return
    await ctx.defer()
    full_command = f"./{SERVER_NAME} {COMMANDS['start']}"
    result = subprocess.run(full_command.split(), cwd=SERVER_PATH, stdout=subprocess.PIPE)
    output = result.stdout.decode()
    output = remove_color_codes(output)  # remove color codes
    chunks = [output[i:i+1900] for i in range(0, len(output), 1900)]
    for chunk in chunks:
        await ctx.send(f"```{chunk}```")

@bot.command(
    name="restart",
    description="Restart the server",
    scope=GUILD_ID,
)
async def restart_server(ctx: interactions.CommandContext):
    if not is_user_allowed(ctx.author.id):
        return
    await ctx.defer()
    full_command = f"./{SERVER_NAME} {COMMANDS['restart']}"
    result = subprocess.run(full_command.split(), cwd=SERVER_PATH, stdout=subprocess.PIPE)
    output = result.stdout.decode()
    output = remove_color_codes(output)  # remove color codes
    chunks = [output[i:i+1900] for i in range(0, len(output), 1900)]
    for chunk in chunks:
        await ctx.send(f"```{chunk}```")

@bot.command(
    name="monitor",
    description="Check server status and restart if crashed",
    scope=GUILD_ID
)
async def monitor_server(ctx: interactions.CommandContext):
    if not is_user_allowed(ctx.author.id):
        return
    await ctx.defer()
    full_command = f"./{SERVER_NAME} {COMMANDS['monitor']}"
    result = subprocess.run(full_command.split(), cwd=SERVER_PATH, stdout=subprocess.PIPE)
    output = result.stdout.decode()
    output = remove_color_codes(output)  # remove color codes
    chunks = [output[i:i+1900] for i in range(0, len(output), 1900)]
    for chunk in chunks:
        await ctx.send(f"```{chunk}```")

@bot.command(
    name="test-alert",
    description="Send a test alert",
    scope=GUILD_ID
)
async def test_alert(ctx: interactions.CommandContext):
    if not is_user_allowed(ctx.author.id):
        return
    await ctx.defer()
    full_command = f"./{SERVER_NAME} {COMMANDS['test-alert']}"
    result = subprocess.run(full_command.split(), cwd=SERVER_PATH, stdout=subprocess.PIPE)
    output = result.stdout.decode()
    output = remove_color_codes(output)  # remove color codes
    chunks = [output[i:i+1900] for i in range(0, len(output), 1900)]
    for chunk in chunks:
        await ctx.send(f"```{chunk}```")

@bot.command(
    name="details",
    description="Display server information",
    scope=GUILD_ID
)
async def server_details(ctx: interactions.CommandContext):
    if not is_user_allowed(ctx.author.id):
        return
    await ctx.defer()
    full_command = f"./{SERVER_NAME} {COMMANDS['details']}"
    result = subprocess.run(full_command.split(), cwd=SERVER_PATH, stdout=subprocess.PIPE)
    output = result.stdout.decode()
    output = remove_color_codes(output)  # remove color codes
    chunks = [output[i:i+1900] for i in range(0, len(output), 1900)]
    for chunk in chunks:
        await ctx.send(f"```{chunk}```")

@bot.command(
    name="stop",
    description="Stop the server",
    scope=GUILD_ID
)
async def stop_server(ctx: interactions.CommandContext):
    if not is_user_allowed(ctx.author.id):
        return
    await ctx.defer()
    full_command = f"./{SERVER_NAME} {COMMANDS['stop']}"
    result = subprocess.run(full_command.split(), cwd=SERVER_PATH, stdout=subprocess.PIPE)
    output = result.stdout.decode()
    output = remove_color_codes(output)  # remove color codes
    chunks = [output[i:i+1900] for i in range(0, len(output), 1900)]
    for chunk in chunks:
        await ctx.send(f"```{chunk}```")

@bot.command(
    name="update-lgsm",
    description="Check and apply any LinuxGSM updates",
    scope=GUILD_ID
)
async def update_lgsm(ctx: interactions.CommandContext):
    if not is_user_allowed(ctx.author.id):
        return
    await ctx.defer()
    full_command = f"./{SERVER_NAME} {COMMANDS['update-lgsm']}"
    result = subprocess.run(full_command.split(), cwd=SERVER_PATH, stdout=subprocess.PIPE)
    output = result.stdout.decode()
    output = remove_color_codes(output)  # remove color codes
    chunks = [output[i:i+1900] for i in range(0, len(output), 1900)]
    for chunk in chunks:
        await ctx.send(f"```{chunk}```")

@bot.command(
    name="update",
    description="Check and apply any server updates",
    scope=GUILD_ID
)
async def update_server(ctx: interactions.CommandContext):
    if not is_user_allowed(ctx.author.id):
        return
    await ctx.defer()
    full_command = f"./{SERVER_NAME} {COMMANDS['update']}"
    result = subprocess.run(full_command.split(), cwd=SERVER_PATH, stdout=subprocess.PIPE)
    output = result.stdout.decode()
    output = remove_color_codes(output)  # remove color codes
    chunks = [output[i:i+1900] for i in range(0, len(output), 1900)]
    for chunk in chunks:
        await ctx.send(f"```{chunk}```")

@bot.command(
    name="check-update",
    description="Check if a gameserver update is available",
    scope=GUILD_ID
)
async def check_update(ctx: interactions.CommandContext):
    if not is_user_allowed(ctx.author.id):
        return
    await ctx.defer()
    full_command = f"./{SERVER_NAME} {COMMANDS['check-update']}"
    result = subprocess.run(full_command.split(), cwd=SERVER_PATH, stdout=subprocess.PIPE)
    output = result.stdout.decode()
    output = remove_color_codes(output)  # remove color codes
    chunks = [output[i:i+1900] for i in range(0, len(output), 1900)]
    for chunk in chunks:
        await ctx.send(f"```{chunk}```")

@bot.command(
    name="force-update",
    description="Apply server updates bypassing check",
    scope=GUILD_ID
)
async def force_update(ctx: interactions.CommandContext):
    if not is_user_allowed(ctx.author.id):
        return
    await ctx.defer()
    full_command = f"./{SERVER_NAME} {COMMANDS['force-update']}"
    result = subprocess.run(full_command.split(), cwd=SERVER_PATH, stdout=subprocess.PIPE)
    output = result.stdout.decode()
    output = remove_color_codes(output)  # remove color codes
    chunks = [output[i:i+1900] for i in range(0, len(output), 1900)]
    for chunk in chunks:
        await ctx.send(f"```{chunk}```")

@bot.command(
    name="validate",
    description="Validate server files with SteamCMD",
    scope=GUILD_ID
)
async def validate_server(ctx: interactions.CommandContext):
    if not is_user_allowed(ctx.author.id):
        return
    await ctx.defer()
    full_command = f"./{SERVER_NAME} {COMMANDS['validate']}"
    result = subprocess.run(full_command.split(), cwd=SERVER_PATH, stdout=subprocess.PIPE)
    output = result.stdout.decode()
    output = remove_color_codes(output)  # remove color codes
    chunks = [output[i:i+1900] for i in range(0, len(output), 1900)]
    for chunk in chunks:
        await ctx.send(f"```{chunk}```")

@bot.command(
    name="backup",
    description="Create backup archives of the server",
    scope=GUILD_ID
)
async def backup_server(ctx: interactions.CommandContext):
    if not is_user_allowed(ctx.author.id):
        return
    await ctx.defer()
    full_command = f"./{SERVER_NAME} {COMMANDS['backup']}"
    result = subprocess.run(full_command.split(), cwd=SERVER_PATH, stdout=subprocess.PIPE)
    output = result.stdout.decode()
    output = remove_color_codes(output)  # remove color codes
    chunks = [output[i:i+1900] for i in range(0, len(output), 1900)]
    for chunk in chunks:
        await ctx.send(f"```{chunk}```")

@bot.command(
    name="mods-update",
    description="Update installed mods/addons",
    scope=GUILD_ID
)
async def mods_update(ctx: interactions.CommandContext):
    if not is_user_allowed(ctx.author.id):
        return
    await ctx.defer()
    full_command = f"./{SERVER_NAME} {COMMANDS['mods-update']}"
    result = subprocess.run(full_command.split(), cwd=SERVER_PATH, stdout=subprocess.PIPE)
    output = result.stdout.decode()
    output = remove_color_codes(output)  # remove color codes
    chunks = [output[i:i+1900] for i in range(0, len(output), 1900)]
    for chunk in chunks:
        await ctx.send(f"```{chunk}```")

def main():
    bot.start()

if __name__ == '__main__':
    main()
