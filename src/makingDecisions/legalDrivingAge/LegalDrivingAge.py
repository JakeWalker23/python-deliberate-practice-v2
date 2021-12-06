class DrivingAge:
    def __init__(self):
        self.__legal_driving_age = 16
        self.driving_age = None
        self.legal_drive = None
        self.success_message = "You are old enough to drive"
        self.unsucessful_message = "You are not old enough to drive"

    def read_driving_age(self):
        self.driving_age = int(input("Please enter your age: "))

    def compare_driving_age(self):
        if self.driving_age >= self.__legal_driving_age:
            self.legal_drive = True
        else:
            self.legal_drive = False

    def display(self):
        print(self.success_message) if self.legal_drive else print(
            self.unsucessful_message)
