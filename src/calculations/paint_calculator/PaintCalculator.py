import math


class Gallons:
    def __init__(self):
        self.__length = 0
        self.__width = 0
        self.__total = 0

    def run(self):
        self.__retrieve_input()
        self.__total = self.__calculate_gallons(self.__length, self.__width)
        self.__print_response_to_std_out(self.__total)

    def __retrieve_input(self):
        print("Welcome to Ceiling paint calculator. Please enter the length and width of your room.")

        self.__length = int(input('What is the length of the room? (in feet)'))
        self.__width = int(input('What is the width of the room? (in feet)'))

    def __calculate_gallons(self, length, width):
        area = length * width

        return math.ceil(area / 350)

    def __print_response_to_std_out(self, response):
        print(f"You need {response} gallons of paint for your ceiling.")

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @property
    def total(self):
        return self.__total
