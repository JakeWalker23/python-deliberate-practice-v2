user_choice = input(
    "Press C to convert from Fahrenheit to Celsius. Pres F to convert from Celsius to Fahrenheit. ")

print(f"Your choice: {user_choice}")

temperature = input("Please enter a temperature: ")

temperature_map = {"F": "Fahrenheit", "C": "Celsius"}

# Calculate the tempeature


def calculate_temperature(choice, temperature):
    if choice == 'F':
        return (int(temperature) * 9 / 5) + 32
    else:
        return (int(temperature) - 32) * (5 / 9)


result = calculate_temperature(user_choice, temperature)
unit_measurement = temperature_map[user_choice]


print(f"The temperature in {unit_measurement} is {result}")
