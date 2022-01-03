class BMI:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        self.bmi_index = None
        self.lower_bmi_range = 18.5
        self.upper_bmi_range = 25

    def prompt_user(self):
        self.height = int(input("What is your height in inches? "))
        self.weight = int(input("What is your weight in lbs? "))

    def calculate_bmi(self):
        self.bmi_index = round(
            (self.weight / (self.height * self.height)) * 703, 2)

    def display_bmi(self):
        if self.bmi_index >= self.lower_bmi_range and self.bmi_index <= self.upper_bmi_range:
            print(f"{self.bmi_index}. You are the ideal weight.")
            return f"{self.bmi_index}. You are the ideal weight."

        elif self.bmi_index < self.lower_bmi_range:
            print(
                f"{self.bmi_index}. You are underweight. Please consult your doctor.")
            return f"{self.bmi_index}. You are underweight. Please consult your doctor."
        else:
            print(
                f"{self.bmi_index}. You are overweight. Please consult your doctor.")
            return f"{self.bmi_index}. You are overweight. Please consult your doctor."
