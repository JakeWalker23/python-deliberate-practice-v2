import math


class Room:
    def __init__(self):
        self.__length = 0.0
        self.__height = 0.0
        self.__area = 0.0
        self.__meter_area = 0.0
        self.__squared_meter_area = 0

    def run(self):
        self.__calculate_area()
        self.__calculate_area_m2()

        print(
            f"You entered dimensions of {self.__length} feet and {self.__height} feet.")
        print(f"The area is {self.__area} square feet.")
        print(f"The square meterage is {self.__meter_area} sqaured meters.")

    def __calculate_area(self):
        self.__length = input("What is the length of the room in feet?")
        self.__height = input("What is the height of the room in feet?")

        self.__area = float(self.__height) * float(self.__length)

    def __calculate_area_m2(self):
        self.__squared_meter_area = self.__area**2 * 0.09290304

        self.__meter_area = math.sqrt(self.__squared_meter_area)

    @property
    def area(self):
        return self.__area

    @property
    def meter_area(self):
        return self.__meter_area

    @property
    def squared_meter_area(self):
        return self.__squared_meter_area
