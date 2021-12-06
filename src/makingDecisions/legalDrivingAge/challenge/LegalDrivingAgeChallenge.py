from src.makingDecisions.legalDrivingAge.challenge.countries import legal_driving_age as countries


class DrivingAge:
    def __init__(self):
        self.__legal_driving_age = 16
        self.driving_age = None
        self.legal_drive = None
        self.success_message = "You are old enough to drive"
        self.unsucessful_message = "You are not old enough to drive"
        self.legal_countries = []

    def read_driving_age(self):
        self.driving_age = int(input("Please enter your age: "))

    def compare_driving_age(self):
        if self.driving_age >= self.__legal_driving_age:
            self.legal_drive = True
        else:
            self.legal_drive = False

    def filter_legal_countries(self):
        for country in countries:
            if countries[country] <= self.driving_age:
                self.legal_countries.append(country)

    def display(self):
        print(f"You are able to drive in {self.legal_countries}") if len(
            self.legal_countries) > 0 else print(self.unsucessful_message)
