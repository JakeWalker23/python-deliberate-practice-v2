class MultiStateTaxCalculator:
    def __init__(self):
        self.__order_amount = 0
        self.__illinois_sales_tax = 0.08
        self.__eau_claire_sales_tax = 0.004
        self.__dunn_sales_tax = 0.005
        self.__state = ''
        self.__county = ''
        self.__total = 0
        
    def run(self):
        self.prompt()
        self.calculateTax()
        self.display()    
    
    def prompt(self):
        self.__order_amount = float(
            input("Please enter the order amount in dollars: "))
        self.__state = input("Please enter your state: ")

        if self.__state == 'Wisconsin' or self.__state == 'wisconsin':
            self.__county = input("Please enter your county: ")

    def calculateTax(self):
        if self.__state == 'Wisconsin':
            if self.__county == 'eau claire':
                self.__total = self.__order_amount + \
                    (self.__order_amount * self.__eau_claire_sales_tax)
            elif self.__county == 'dunn':
                self.__total = self.__order_amount + \
                    (self.__order_amount * self.__dunn_sales_tax)
            else:
                self.__total = self.__order_amount

        elif self.__state == 'Illinois':
            self.__total = self.__order_amount + \
                (self.__order_amount * self.__illinois_sales_tax)
        else:
            self.__total = self.__order_amount

    def display(self):
        print(f"the total is ${self.__total}")

    @property
    def order_amount(self):
        return self.__order_amount
    
    @property
    def state(self):
        return self.__state
    
    @property
    def total(self):
        return self.__total
    
    @property
    def county(self):
        return self.__county
    
    @property
    def illinois_sales_tax(self):
        return self.__illinois_sales_tax
    
    @property
    def eau_claire_sales_tax(self):
        return self.__eau_claire_sales_tax 
        
    @property
    def dunn_sales_tax(self):
        return self.__dunn_sales_tax