from decimal import Decimal

amount_to_convert = input("How many pounds are you exchanging?")

exchange_rate = input("What is the exchange rate?")


def calculate_currency(amount_to_convert, exchange_rate):
    return round(int(amount_to_convert) * float(exchange_rate), 2)


return_currency = calculate_currency(amount_to_convert, exchange_rate)

print(f"{amount_to_convert} Pounds at an exchange rate of {exchange_rate} is {return_currency} US Dollars")
