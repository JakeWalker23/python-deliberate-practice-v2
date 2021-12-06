from decimal import Decimal


class TaxCalculator:
    def __init__(self):
        self.order_amount = 0
        self.state = ''
        self.wisconsin_values = ["WI", "Wi",
                                 "wi", "wI", "Wisconsin", "wisconsin"]
        self.TAX_PERCENTAGE = 0.055
        self.total = 0
        self.nl = '\n'

    def read_input(self):
        self.order_amount = input("Please enter an order amount: ")
        self.state = input("Please enter an US State: ")

    def compute_total(self):
        if self.state in self.wisconsin_values:
            self.total = float(self.order_amount) + \
                (float(self.order_amount) * self.TAX_PERCENTAGE)
            return
        self.total = self.order_amount

    def display_total(self):
        if self.state in self.wisconsin_values:
            print(
                f"The subtotal is £{self.order_amount} {self.nl} The tax amount is £{float(self.order_amount) * self.TAX_PERCENTAGE} {self.nl} The total is £{self.total}")
        if self.state not in self.wisconsin_values:
            print(
                f"The subtotal is £{self.order_amount} {self.nl} The total is £{self.total}")
