class BMI:
    def __init__(self):
        self.__height = 0 
        self.__weight = 0
        self.__bmi_index = None
        self.__lower_bmi_range = 18.5
        self.__upper_bmi_range = 25
        
    def run(self):
        self.prompt_user()
        self.calculate_bmi()
        self.display_bmi()

    def prompt_user(self):
        self.__height = int(input("What is your height in inches? "))
        self.__weight = int(input("What is your weight in lbs? "))

    def calculate_bmi(self):
        self.__bmi_index = round(
            (self.__weight / (self.__height * self.__height)) * 703, 2)

    def display_bmi(self):
        if self.__bmi_index >= self.__lower_bmi_range and self.__bmi_index <= self.__upper_bmi_range:
            print(f"{self.__bmi_index}. You are the ideal weight.")
            return f"{self.__bmi_index}. You are the ideal weight."

        elif self.__bmi_index < self.__lower_bmi_range:
            print(
                f"{self.__bmi_index}. You are underweight. Please consult your doctor.")
            return f"{self.__bmi_index}. You are underweight. Please consult your doctor."
        else:
            print(
                f"{self.__bmi_index}. You are overweight. Please consult your doctor.")
            return f"{self.__bmi_index}. You are overweight. Please consult your doctor."


    @property
    def height(self):
        return self.__height
    
    @property
    def weight(self):
        return self.__weight
    
    @property
    def bmi_index(self):
        return self.__bmi_index
    
    @property
    def lower_bmi_range(self):
        return self.__lower_bmi_range
    
    @property
    def upper_bmi_range(self):
        return self.__upper_bmi_range