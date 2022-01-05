class TroubleshootCarIssues:
    def __init__(self):
        self.choice = ''
        self.answer = ''

    def troubleshoot_car_issues(self):
        print("Welcome to the car troubleshooting program.")
        print("Please enter y for yes or n for no")
        print("")
        self.choice = input("Is the car silent when you turn the key?")

        if self.choice == 'y':

            self.choice = input("Are the battery terminals corroded?")

            if self.choice == 'y':
                self.answer = "Clean terminals and try starting again."
                print(self.answer)

            elif self.choice == 'n':
                self.answer = "Replace cables and try again."
                print(self.answer)
                return

        if self.choice == 'n':

            self.choice = input("Does the car make a clicking noise?")

            if self.choice == 'y':

                self.answer = "Replace the battery."
                print(self.answer)

            elif self.choice == 'n':

                self.choice = input("Does the car crank up but fail to start?")

                if self.choice == 'y':

                    self.answer = "Check spark plug connections."
                    print(self.answer)

                elif self.choice == 'n':

                    self.choice = input(
                        "Does the engine start up and then die?")

                    if self.choice == 'y':

                        self.choice = input(
                            "Does your car have fuel injection?")

                        if self.choice == 'y':

                            self.answer = "Get it in for service."
                            print(self.answer)

                        elif self.choice == 'n':
                            self.answer = 'Check to ensure the choke is opening and closing.'
                            print(self.answer)

                    elif self.choice == 'n':
                        self.answer = 'See a specialist.'
                        print(self.answer)
