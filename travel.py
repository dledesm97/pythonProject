import translator
import countries
import distance
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
            print("1. Translator")
            print("2. Find Distance Between Locations")
            print("3. Quick Facts")
            print("4. Currency Exchange")
            print("5. Exit Program")
            userInput = input("Your choice: ")
            if userInput == "1":
                translator.menu()   #this function is in the translator.py file and we are calling it from here 
            elif userInput == "2":
                distance.find_distance()    #calling the find_distance function from the distance file
            elif userInput == "3":
                information.quick_facts(country)
            elif userInput == "4":
                currency.currency_converter()
            elif userInput == "5":
                exit()              # killing the program if the user enters 5
            else:
                print("Choice not found")
        except KeyboardInterrupt:
            print("Exiting Program")
        
if __name__ == '__main__':
   homepage()
#homepage()
