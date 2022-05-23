from multiprocessing.sharedctypes import Value
from src.makingDecisions.numbersToMonths.resources.months import months
import sys


class NumbersToMonths:
    def __init__(self):
        self.__user_choice = ""
        self.__converted_month = ""
        self.errors = []

    def run(self):
        self.prompt()
        self.convert_to_month()
        self.display()

    def prompt(self):
        print("Welcome to number to months. Please enter a number to be converted into its month representation")

        self.__user_choice = int(input(
            "Please enter the number of the month: "))

    def convert_to_month(self):
        try:
            self.__converted_month = months[self.user_choice]
        except ValueError as e:
            self.errors.append(str(e))
            sys.exit(str(e))

    def display(self):
        if len(self.errors) == 0:
            print(f"The month of the year is {self.converted_month}")
        else:
            print(
                f"Sorry, {self.user_choice} is not a valid month of the year")

            return False

    @property
    def user_choice(self):
        return self.__user_choice

    @property
    def converted_month(self):
        return self.__converted_month
