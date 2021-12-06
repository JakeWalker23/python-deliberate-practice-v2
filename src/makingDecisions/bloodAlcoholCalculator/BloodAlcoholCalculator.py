print("Welcome to the Blood Alcohol Calculator.")
MALE_BAC = 0.73
FEMALE_BAC = 0.66

weight = int(input("Please enter your weight in lbs: "))
gender = input("Please enter your gender: ")
number_of_drinks = int(
    input("Please enter the number of drinks you have had: "))
alcohol_percentage = int(input("Please enter the alcohol percentage: "))
time_elapsed = int(
    input("Please enter the time elapsed since last drink: (In hours) "))


def calculate_blood_alcohol(weight, number_of_drinks, alcohol_percentage, time_elapsed):
    return ((number_of_drinks * alcohol_percentage * 0.075 / weight) - 0.015 * time_elapsed)


blood_alcohol_rate = calculate_blood_alcohol(
    weight, number_of_drinks, alcohol_percentage, time_elapsed)


def print_blood_alcohol_limit(gender, blood_alcohol_rate):
    if gender == "male":
        if blood_alcohol_rate > MALE_BAC:
            return "You are over the limit"
        else:
            return "You are under the limit"

    if gender == "female":
        if blood_alcohol_rate > FEMALE_BAC:
            return "You are over the limit"
        else:
            return "You are under the limit "


result = print_blood_alcohol_limit(gender, blood_alcohol_rate)
