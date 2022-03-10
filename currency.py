from currency_converter import CurrencyConverter
import currencies

output = currencies.CURRENCIES
def currency_converter():
    print("1. Exchange")
    print("2. List of Currencies")
    user_input = int(input("Make your selection: "))
    if user_input == 1:
        c = CurrencyConverter()
        print("Exchange Your Currency")
        current = (input("Current Currency: ")).upper()
        future = (input("Expected Currency: ")).upper()
        amount = float(input("How much do you want to exchange? "))
        exchanged_amount = c.convert(amount, current, future)
        print(f"{amount} {current} = {exchanged_amount} {future}")
    if user_input == 2:
        print(output)
        currency_converter()
