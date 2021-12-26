import decimal


class MultiStateTaxCalculator:
    def __init__(self):
        self.order_amount = 0
        self.illinois_sales_tax = 0.08
        self.eau_claire_sales_tax = 0.004
        self.dunn_sales_tax = 0.005
        self.state = ''
        self.county = ''
        self.total = 0

    def prompt(self):
        self.order_amount = float(
            input("Please enter the order amount in dollars: "))
        self.state = input("Please enter your state: ")

        if self.state == 'Wisconsin' or self.state == 'wisconsin':
            self.county = input("Please enter your county: ")

    def calculateTax(self):
        if self.state == 'Wisconsin':
            if self.county == 'eau claire':
                self.total = self.order_amount + \
                    (self.order_amount * self.eau_claire_sales_tax)
            elif self.county == 'dunn':
                self.total = self.order_amount + \
                    (self.order_amount * self.dunn_sales_tax)
            else:
                self.total = self.order_amount

        elif self.state == 'Illinois':
            self.total = self.order_amount + \
                (self.order_amount * self.illinois_sales_tax)
        else:
            self.total = self.order_amount

    def display(self):
        print(f"the total is ${self.total}")
