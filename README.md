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
   pip install LinuxGSM-discord-bot/DGSbot-2.0.tar.gz
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
   
# Usage

The bot listens for messages starting with the "!" symbol. The available commands are:

| Command | Shortcut | Description |
|---------|----------|-------------|
| start | st | Start the server. |
| restart | r | Restart the server. |
| monitor | m | Check server status and restart if crashed. |
| test-alert | ta | Send a test alert. |
| details | dt | Display server information. |
| postdetails | pd | Post details to termbin.com (removing passwords). |
| skeleton | sk | Create a skeleton directory. |
| update-lgsm | ul | Check and apply any LinuxGSM updates. |
| update | u | Check and apply any server updates. |
| check-update | cu | Check if a gameserver update is available. |
| force-update | fu | Apply server updates bypassing check. |
| validate | v | Validate server files with SteamCMD. |
| backup | b | Create backup archives of the server. |
| console | c | Access server console. |
| debug | d | Start server directly in your terminal. |
| mods-install | mi | View and install available mods/addons. |
| mods-remove | mr | View and remove an installed mod/addon. |
| mods-update | mu | Update installed mods/addons. |
| install | i | Install the server. |
| auto-install | ai | Install the server without prompts. |
| developer | dev | Enable developer mode. |
| stop | sp | Stop the server. |

To execute a command, simply type the command name or its corresponding shortcut after the "!" symbol. For example, to start the server, you can use either `!start` or `!st`.

## Contributing

If you find a bug or have a suggestion, please open an issue on GitHub. Pull requests are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/sarangcr03/LinuxGSM-discord-bot/blob/main/License) file for details.
