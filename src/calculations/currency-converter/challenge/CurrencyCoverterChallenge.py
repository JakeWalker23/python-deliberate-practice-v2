from decimal import Decimal

exchange_lookup = {
    "uk": 1.3865,
    "france": 1.19,
    "poland": 0.26,
    "australia": 0.74,
    "canada": 0.80,
    "china": 0.15,
    "new zealand": 0.71,
    "russia": 0.014
}

while True:

    country = input("Please enter a country for exchange with US Dollars ")

    if country not in exchange_lookup:
        print(
            f"Sorry, we do not provide exchange rates for {country}. Please enter another. ")
        country = input("Please enter a country for exchange with US Dollars ")

    amount_to_convert = input("Please enter the amount for exchange ")

    def calculate_currency(country, amount_to_convert):
        return round(int(amount_to_convert) * float(exchange_lookup[country.lower()]), 2)

    return_currency = calculate_currency(country, amount_to_convert)

    print(f"{amount_to_convert} at an exchange rate from {country} is ${return_currency} US Dollars")
