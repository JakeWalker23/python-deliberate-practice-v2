class TemperatureConverter:
    def __init__(self):
        self.__metric = "C"
        self.__temperature = 0
        self.__result = 0
        
    def run(self):
        self.read_user_input()
        self.__result = self.calculate_temperature()
        self.display_temperature_to_user()
            
    def read_user_input(self):
        self.__metric = input("Press C to convert from Fahrenheit to Celsius. Pres F to convert from Celsius to Fahrenheit. ")
        self.__temperature = input("Please enter a temperature: ")
        
    def metric_map(self, metric):
        metric_map = {"F": "Fahrenheit", "C": "Celsius"}
        
        return metric_map[metric]
    
    def calculate_temperature(self):
        if self.__metric == 'F':
            return (int(self.__temperature) * 9 / 5) + 32
        else:
            return (int(self.__temperature) - 32) * (5 / 9)

    def display_temperature_to_user(self):
        unit_measurement = self.metric_map(self.__metric)
        print(f"The temperature in {unit_measurement} is {self.__result}")
        
    @property
    def metric(self):
        return self.__metric
    
    @property
    def temperature(self):
        return self.__temperature
    
    @property
    def result(self):
        return self.__result