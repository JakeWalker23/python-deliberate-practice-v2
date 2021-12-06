import math
from decimal import Decimal

tax_rate = 5.5

print('Welcome! Please enter 3 items you wish to calculate')

item_1 = input('Please enter the price of item #1 ')
quantity_1 = input('Please enter the quantity of item #1 ')

print(int(item_1) * int(quantity_1))

item_2 = input('Please enter the price of item #2 ')
quantity_2 = input('Please enter the quantity of item #2 ')

print(int(item_2) * int(quantity_2))

item_3 = input('Please enter the price of item #3 ')
quantity_3 = input('Please enter the quantity of item #3 ')

print(int(item_3) * int(quantity_3))


def calculate_sub_total(user_item_1, user_quantity_1, user_item_2, user_quantity_2, user_item_3, user_quantity_3):
    basket_1 = int(user_item_1) * int(user_quantity_1)
    basket_2 = int(user_item_2) * int(user_quantity_2)
    basket_3 = int(user_item_3) * int(user_quantity_3)

    return basket_1 + basket_2 + basket_3


sub_total = calculate_sub_total(
    item_1, quantity_1, item_2, quantity_2, item_3, quantity_3)


def calculate_tax_cost(sub_total_amount, tax_rate):
    tax_rate = tax_rate / 100
    print(tax_rate)
    return round(sub_total_amount * tax_rate, 2)


tax_to_add = calculate_tax_cost(sub_total, tax_rate)


def calculate_total(tax, sub_total_cost):
    return round(tax + sub_total_cost, 2)


total = calculate_total(tax_to_add, sub_total)


print(f"The sub total amount is: {sub_total}")

print(f"The tax amount is: {tax_to_add}")

print(f"The total cost to pay is: {total}")
