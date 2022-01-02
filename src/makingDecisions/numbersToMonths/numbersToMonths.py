from src.makingDecisions.numbersToMonths.resources.months import months


class NumbersToMonths:
    def __init__(self):
        self.months = months
        self.user_choice = ""
        self.converted_month = ""

    def prompt(self):
        self.user_choice = int(input("Please enter the number of the month: "))

    def convert_to_month(self):
        self.converted_month = self.months[self.user_choice]

    def display(self):
        print(f"The month of the year is {self.converted_month}")
