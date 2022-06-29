from calendar import month
import math


class CreditCard:
    def __init__(self):
        self.__balance = 0
        self.__apr = 0
        self.__monthly_repayment = 0

    def run(self):
        self.read_user_input()
        self.calculate_repayment_duration(
            self.__balance, self.__apr, self.__monthly_repayment)

    def read_user_input(self):
        self.__balance = input("What is your current balance?")
        self.__apr = input("What percent is your APR?")
        self.__monthly_repayment = input("How much do you repay each month?")

    def calculate_repayment_duration(self, balance, apr, monthly_repayment):
        __first = -(1/30)
        __daily_rate = (int(apr) / 365)
        __bottom = math.log(1 + __daily_rate)
        __b_over_p = (int(balance) / int(monthly_repayment))
        __second_daily_rate = math.pow((1 + __daily_rate), 30)

        print({"First": __first})

        print({"Daily Rate": __daily_rate})
        print({"Bottom": __bottom})
        print({"B / P ": __b_over_p})
        print({"Second Daily Rate": __second_daily_rate})

        calc = (__b_over_p * (1 - __second_daily_rate))

        print({"Calc": calc})
        return calc
        top = math.log(1 + calc)
        print({"Top Line": top})

        return __first * top

    @ property
    def balance(self):
        return self.__balance

    @ property
    def apr(self):
        return self.__apr

    @property
    def monthly_repayment(self):
        return self.__monthly_repayment
