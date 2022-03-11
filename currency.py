from currency_converter import CurrencyConverter
import currencies   #importing currencies file
import travel

output = currencies.CURRENCIES
def currency_converter():
    try:
        while True:
            print("{:-^30}".format("-"))
            #listing out the available options when converting
            print("1. Exchange")
            print("2. List of Currencies")
            print("3. Exit Program")
            print("{:-^30}".format("-"))
            user_input = input("Make your selection: ")
            if user_input == "1":
                counter = 0
                c = CurrencyConverter() #creating an instance of currency converter
                print("Exchange Your Currency")
                current =(input("Current Currency: ")).upper() #the currency must be all uper-case
                for x in output:
                    if current == x:
                        counter += 1            # checking if the currency that was inputted is in the 
                        continue                # list of availble currencies    
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
                print("{:-^30}".format("-"))
                print(f"{amount} {current} = {exchanged_amount} {future}")
            elif user_input == "2":
                print("{:-^30}".format("-"))
                print("{:^30}".format("List Of Currencies"))
                print(', '.join(output))
                currency_converter()
            elif user_input == "3":
                exit()
            else:
                print("Choice not found")
    except KeyboardInterrupt:
        print("Exiting")
