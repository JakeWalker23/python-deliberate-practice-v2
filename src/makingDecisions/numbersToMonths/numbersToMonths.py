from src.makingDecisions.numbersToMonths.resources.months import months


class NumbersToMonths:
    def __init__(self):
        self.months = months
        self.user_choice = ""
        self.converted_month = ""
        self.errors = []

    def prompt(self):
        self.user_choice = int(input("Please enter the number of the month: "))

    def convert_to_month(self):
        try:
            self.converted_month = self.months[self.user_choice]
        except KeyError as e:
            self.errors.append(e)

    def display(self):
        if len(self.errors) == 0:
            print(f"The month of the year is {self.converted_month}")
        else:
            print(
                f"Sorry, {self.user_choice} is not a valid month of the year")
