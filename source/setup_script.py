import os
import dotenv

def setup():
    dotenv_path = os.path.expanduser('~/.env')
    with open(dotenv_path, 'w') as f:
        token = input('Enter your Discord bot token: ')
        print(f"TOKEN={token}")
        f.write(f"TOKEN={token}\n")
        
        server_path = input('Enter your server path: ')
        print(f"SERVER_PATH={server_path}")
        f.write(f"SERVER_PATH={server_path}\n")
        
        server_name = input('Enter your server name: ')
        print(f"SERVER_NAME={server_name}")
        f.write(f"SERVER_NAME={server_name}\n")
        
        allowed_user_ids = input('Enter your allowed user IDs: ')
        print(f"ALLOWED_USER_IDS={allowed_user_ids}")
        f.write(f"ALLOWED_USER_IDS={allowed_user_ids}\n")
        
        while True:
            try:
                guild_id = int(input('Enter the guild ID for slash commands: '))
                break
            except ValueError:
                print("Please enter a valid integer value.")
        print(f"GUILD_ID={guild_id}")
        f.write(f"GUILD_ID={guild_id}\n")


if __name__ == '__main__':
    setup()
