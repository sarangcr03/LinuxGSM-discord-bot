# DGSbot

DGSbot is a Discord bot that helps you manage your game servers. It allows you to run server commands directly from Discord, without the need to access the server console. 

## Requirements

To use DGSbot, you need the following:

- Python 3.6 or higher
- A Discord bot token
- Access to the server where your game server is hosted

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/DGSbot.git
   ```

2. Install the package:

   ```
   pip install -e .
   ```

3. Run the setup script to set your environment variables:

   ```
   DGSbot-setup
   ```

   You will be prompted to enter your Discord bot token, server path, server name, and allowed user IDs.

4. Start the bot:

   ```
   nohup DGSbot &
   ```

   This will start the bot in the background and detach it from the terminal. If you want to stop the bot later, you can use the `kill` or `pkill` command.
   

## Usage

Once the bot is running, you can use the following commands in Discord:

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

## Contributing

If you find a bug or have a suggestion, please open an issue on GitHub. Pull requests are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
