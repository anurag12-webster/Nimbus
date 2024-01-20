from password_manager.manager import User
from password_manager.storage import *
from colorama import Fore

def main():
    create_table()

    if credentials_exist():
        username = input(Fore.BLUE + "Enter your username: ")
        password = input(Fore.GREEN + "Enter your password: ")

        if verify_credentials(username, password):
            print("Login successful!")
            
        else:
            print("Invalid credentials. Exiting...")
    else:
        print("Not found in existing. Create your profile.")
        user = User.create_user()
        save_credentials(user)
        print("Account created successfully!")

if __name__ == "__main__":
    main()
