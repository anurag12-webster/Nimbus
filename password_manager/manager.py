from colorama import Fore

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def create_user():
        username = input(Fore.GREEN + "Username: ")
        password = input(Fore.GREEN + "Credential: ")
        return User(username, password)

    def verify_credentials(self, entered_username, entered_password):
        return self.username == entered_username and self.password == entered_password
