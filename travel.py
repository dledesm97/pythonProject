import translator
import countries
import information
import currency
import os

#importing the countries from the countries file in the same directory
destination = countries.COUNTRIES

def homepage():
    try:
        print("{:-^100}".format("-"))
        print("{:^100}".format("Where are you traveling?"))
        print("{:-^100}".format("-"))

        #display all the available countries for this program
        print(' '.join(destination))

        #asking for user input and making it all uppercase when storing it in the variable
        country = (input("\nFrom the options above, please type your destination: ")).upper()
        # keeping track of the user input and looping through the countries list
        # to make sure it matches with at least one country if NOT ask for user input again
        counter = 0
        for x in destination:
            if country == x:
                counter = 1
                selection(country)
        if (counter == 0):
            print("Please enter a valid country")
            homepage()
    except KeyboardInterrupt:
        print("Exiting Program")

# Outputting the list of options that the user can do in this program
def selection(country):
    while True:
        try:
            options = ["1. Translator", "2. Quick Facts", "3. Currency Exchange", "4. Exit Program"]
            print('\n'.join(options))
            userInput = input("Your choice: ")
            if userInput == "1":
                translator.menu()   #this function is in the translator.py file and we are calling it from here 
            elif userInput == "2":
                information.quick_facts(country)
            elif userInput == "3":
                currency.currency_converter()
            elif userInput == "4":
                exit()              # killing the program if the user enters 5
            else:
                print("Choice not found")
        except KeyboardInterrupt:
            print("Exiting Program")
        
if __name__ == '__main__':
   homepage()
#homepage()
