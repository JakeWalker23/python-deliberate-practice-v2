number_of_people = input('How many people are there?')

number_of_pizzas = input('How many pizzas are there?')

number_of_slices = input('How many slices per pizza are there?')


while (int(number_of_slices) % 2) is not 0:

    number_of_slices = input(
        'How many slices per pizza? Please enter an even number')


print(f"there are {number_of_people} people with {number_of_pizzas} pizzas")

slices_per_person = (int(number_of_slices) /
                     int(number_of_people)) * int(number_of_pizzas)

print(
    f"Each person will receive {slices_per_person} slices of pizza per person!")

print('There will be 0 slices left over')
