from currency_converter import CurrencyConverter
import currencies
import travel

output = currencies.CURRENCIES
def currency_converter():
    try:
        while True:
            print("1. Exchange")
            print("2. List of Currencies")
            print("3. Exit Program")
            user_input = input("Make your selection: ")
            if user_input == "1":
                counter = 0
                c = CurrencyConverter()
                print("Exchange Your Currency")
                current =(input("Current Currency: ")).upper()
                for x in output:
                    if current == x:
                        counter += 1
                        continue
                future = (input("Expected Currency: ")).upper()
                for y in output:
                    if future == y:
                        counter += 1
                        continue
                if counter < 2:
                    print("Input availabe currencies")
                    currency_converter()
                amount = float(input("How much do you want to exchange? "))
                exchanged_amount = c.convert(amount, current, future)
                print(f"{amount} {current} = {exchanged_amount} {future}")
            elif user_input == "2":
                print(output)
                currency_converter()
            elif user_input == "3":
                exit()
            else:
                print("Choice not found")
    except KeyboardInterrupt:
        print("Exiting")
