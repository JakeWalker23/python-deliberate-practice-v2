from src.making_decisions.legal_driving_age.resources.countries import legal_driving_age as countries


class DrivingAge:
    def __init__(self):
        self.__minimum_driving_age = 16
        self.__driving_age = None
        self.__legal_drive = None
        self.success_message = "You are old enough to drive"
        self.unsucessful_message = "You are not old enough to drive"
        self.__legal_countries = []
        
    def run(self):
        self.read_driving_age()
        self.compare_driving_age()
        self.filter_legal_countries()
        self.display()

    def read_driving_age(self):
        self.__driving_age = int(input("Please enter your age: "))

    def compare_driving_age(self):
        if self.__driving_age >= self.__minimum_driving_age:
            self.__legal_drive = True
        else:
            self.__legal_drive = False

    def filter_legal_countries(self):
        for country in countries:
            if countries[country] <= self.__driving_age:
                self.__legal_countries.append(country)

    def display(self):
        print(f"You are able to drive in {self.__legal_countries}") if len(
            self.__legal_countries) > 0 else print(self.unsucessful_message)

    @property
    def minimum_driving_age(self):
        return self.__minimum_driving_age
    
    @property
    def driving_age(self):
        return self.__driving_age
    
    @property
    def legal_drive(self):
        return self.__legal_drive
    
    @property
    def legal_countries(self):
        return self.__legal_countries
    