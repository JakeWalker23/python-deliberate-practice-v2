import math

# Store formula in here
# meters*2 = feet*2 * 0.09290304

while True:

    length = input("What is the length of the room in feet?")

    height = input("What is the height of the room in feet?")

    print(f"You entered dimensions of {length} feet and {height} feet.")

    square_feet_area = int(length) * int(height)

    print("The area is " + str(square_feet_area) + " square feet.")

    squared_meter_area = square_feet_area**2 * 0.09290304
    meter_area = math.sqrt(squared_meter_area)

    print("The square meterage is " + str(meter_area) + " sqaured meters.")
