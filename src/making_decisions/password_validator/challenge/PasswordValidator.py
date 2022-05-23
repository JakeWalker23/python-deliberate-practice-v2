from valid_passwords import passwords
import getpass
from cryptography.fernet import Fernet


class Credentials:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.valid_username = False
        self.valid_password = False
        self.key = Fernet.generate_key()

    def read_credentials(self):
        self.username = input("Please enter your username: ")
        self.password = getpass.getpass(prompt='Please enter your password: ')

    def validate(self):
        if self.username in passwords:
            self.valid_username = True
        else:
            return

        if self.password == passwords[self.username]:
            self.valid_password = True
        print(passwords[self.username])

    def encrypt(self):
        fernet = Fernet(self.key)
        self.password = fernet.encrypt(self.password.encode())
        print(self.password)

    def display(self):
        if self.valid_username == True and self.valid_password == True:
            print(f"Welcome, {self.username}!")
        elif self.valid_username == True and self.valid_password == False:
            print(f"Sorry, password invalid. Please try again")
        else:
            print(
                f"Sorry, {self.username} is not in our system. Please try again.")
