from decimal import Decimal

class TaxCalculator:
    def __init__(self):
        self.__order_amount = 0
        self.__state = ""
        self.__TAX_PERCENTAGE = 0.055
        self.wisconsin_values = ["WI", "Wi",
                                 "wi", "wI", "Wisconsin", "wisconsin"]
        self.__total = 0
        self.nl = '\n'
        
    def run(self):
        self.read_user_input()
        self.compute_tax_on_order()
        
        self.display_total()
        
    def read_user_input(self):
        self.__order_amount = input("Please enter an order amount:")
        self.__state = input("Please enter a US State:")
        
    def compute_tax_on_order(self):
        if self.__state in self.wisconsin_values:
            self.__total = float(self.__order_amount) + (float(self.__order_amount) * self.__TAX_PERCENTAGE)
            return
        
        self.__total = float(self.__order_amount)

    def display_total(self):
        if self.__state in self.wisconsin_values:
            print(
                f"The subtotal is £{self.__order_amount} {self.nl} The tax amount is £{float(self.__order_amount) * self.__TAX_PERCENTAGE} {self.nl} The total is £{self.__total}")
        if self.__state not in self.wisconsin_values:
            print(
                f"The subtotal is £{self.__order_amount} {self.nl} The total is £{self.__total}")

    @property
    def order_amount(self):
        return self.__order_amount
    
    @property
    def state(self):
        return self.__state
    
    @property
    def tax_percentage(self):
        return self.__TAX_PERCENTAGE
    
    @property
    def total(self):
        return self.__total