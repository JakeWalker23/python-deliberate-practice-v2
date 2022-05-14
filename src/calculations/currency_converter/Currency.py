from ast import ExceptHandler
from src.calculations.currency_converter.resources.exchange_lookup import exchange_lookup
import sys


class Currency:
    def __init__(self):
        self.__country = ""
        self.__convert_amount = 0.0
        self.__converted_currency = 0.0

    def run(self):
        self.__retrieve_input()
        self.__converted_currency = self.__convert_currency()

        print(f"{self.__convert_amount} at an exchange rate from {self.__country} is ${self.__converted_currency} US Dollars")

    def __retrieve_input(self):
        self.__country = input(
            "Please enter a country for exchange with US Dollars ")

        self.__convert_amount = input(
            "Please enter the amount for exchange ")

        if self.__country not in exchange_lookup:
            print(
                f"Sorry, we do not provide exchange rates for {self.__country}. Please enter another. ")

            sys.exit("Invalid Country provided")

    def __convert_currency(self):
        exchange_rate = exchange_lookup[self.__country.lower()]

        return self.__convert_amount * exchange_rate

    @property
    def country(self):
        return self.__country

    @property
    def convert_amount(self):
        return self.__convert_amount

    @property
    def converted_currency(self):
        return self.__converted_currency
