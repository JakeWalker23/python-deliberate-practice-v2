class Credentials:
    '''Credential class to validate username and password'''

    def __init__(self):
        self.username = ""
        self.password = ""
        self.valid_username = False
        self.valid_password = False

    def read_credentials(self):
        self.username = input("Please enter your username: ")
        self.password = input("Please enter your password: ")

    def validate(self):
        if self.username == "JakeWalker":
            self.valid_username = True
        else:
            return

        if self.password == "12345":
            self.valid_password = True

    def display(self):
        if self.valid_username == True and self.valid_password == True:
            print(f"Welcome, {self.username}!")
        elif self.valid_username == True and self.valid_password == False:
            print(f"Sorry, password invalid. Please try again")
        else:
            print(
                f"Sorry, {self.username} is not in our system. Please try again.")
