# UNMAINTAINED SINCE 2023 
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
   pip install LinuxGSM-discord-bot/DGSbot-2.5.tar.gz
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

The available commands are:

| Command | Description |
|---------|-------------|
| /stop | Stop the server. |
| /start | Start the server. |
| /restart | Restart the server. |
| /monitor | Check server status and restart if crashed. |
| /test-alert | Send a test alert. |
| /details | Display server information. |
| /update-lgsm | Check and apply any LinuxGSM updates. |
| /update | Check and apply any server updates. |
| /check-update | Check if a gameserver update is available. |
| /force-update | Apply server updates bypassing check. |
| /validate | Validate server files with SteamCMD. |
| /backup | Create backup archives of the server. |
| /mods-update | Update installed mods/addons. |

## Contributing

If you find a bug or have a suggestion, please open an issue on GitHub. Pull requests are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/sarangcr03/LinuxGSM-discord-bot/blob/main/License) file for details.
