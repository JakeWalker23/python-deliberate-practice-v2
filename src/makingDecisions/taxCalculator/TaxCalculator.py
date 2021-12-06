from decimal import Decimal

TAX_PERCENTAGE = 0.055

order_amount = input("Please enter an order amount: ")
state = input("Please enter a state: ")


def compute_total(order_amount, state):
    if state == 'wi':
        return float(order_amount) + (float(order_amount) * TAX_PERCENTAGE)
    return order_amount


total = compute_total(order_amount, state)

nl = '\n'

if state == 'wi':
    print(
        f"The subtotal is £{order_amount} {nl} The tax amount is £{float(order_amount) * TAX_PERCENTAGE} {nl} The total is £{total}")

if state != 'wi':
    print(f"The subtotal is £{order_amount} {nl} The total is £{total}")
