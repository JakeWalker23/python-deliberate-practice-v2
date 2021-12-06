import math


def calculate_gallons(length, width):
    total = int(length) * int(width)
    gallons = math.ceil(total / 350)

    return gallons


while True:
    length = input('What is the length of the room? (in feet)')
    width = input('What is the width of the room? (in feet)')

    GALLONS = calculate_gallons(length, width)

    print(f"You need {GALLONS} gallons of paint for your ceiling")
