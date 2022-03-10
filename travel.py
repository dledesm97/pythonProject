import translator
import countries
import distance
import information
import currency
import os

destination = countries.COUNTRIES
def homepage():
    print("{:-^100}".format("-"))
    print("{:^100}".format("Where are you traveling?"))
    print("{:-^100}".format("-"))
    #display all the available countries for this program
    print(' '.join(destination))
    country = (input("\nFrom the options above, please type your destination: ")).upper()
    counter = 0
    for x in destination:
        if country == x:
            counter = 1
            selection(country)
    if (counter == 0):
        print("Please enter a valid country")
        homepage()
        
    
    #os.system('clear')
    
def selection(country):
    print("1. Translator")
    print("2. Find Distance Between Locations")
    print("3. Quick Facts")
    print("4. Currency Exchange")
    print("5. Exit Program")
    userInput = int(input("Your choice: "))
    if userInput == 1:
        translator.menu()
    if userInput == 2:
        distance.find_distance()
    if userInput == 3:
        information.quick_facts(country)
    if userInput == 4:
        currency.currency_converter()
    if userInput == 5:
        exit()
#if __name__ == '__main__':
   #homepage()
   #titles()
   #menu()
homepage()
