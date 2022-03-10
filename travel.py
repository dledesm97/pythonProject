from googletrans import Translator
from geopy.distance import geodesic
from countryinfo import CountryInfo
from currency_converter import CurrencyConverter
import language
import os

language = language.LANGUAGES
translator = Translator()

def menu():
    print("Main Program")
    while True:
        print('\a')
        print("{:-^30}".format("-"))
        print("Choice")
        print("1. Translate languages")
        print("2. Available languages")
        print("3. Exit program")
        print("{:-^30}".format("-"))
        print("\a")
        choose = input("Your choice: ")

        if choose == "1":
            titles()
            pair_language()
        elif choose == "2":
            language_title()
            all_symbol()
        elif choose == "3":
            print("Have a good day!")
            exit()
        else:
            print("Choice not found")

def homepage():
    print("{:-^30}".format("-"))
    print("{:^30}".format("Where are you traveling?"))
    print("{:-^30}".format("-"))
    
    destination = input("Enter the location: ")
    os.system('clear')
    
    print("1. Translator")
    print("2. Find Distance Between Locations")
    print("3. Quick Facts")
    print("4. Currency Exchange")
    userInput = int(input("Your choice: "))
    if userInput == 1:
        menu()
    if userInput == 2:
        find_distance()
    if userInput == 3:
        quick_facts(destination)
    if userInput == 4:
        currency_converter()
    
def titles():
    #os.system('clear')
    print("{:-^30}".format("-"))
    print("{:^30}".format("Let me help you translate"))
    print("{:-^30}".format("-"))
    
def language_title():
    print("{:-^30}".format("-"))
    print("{:^30}".format("Available Languages"))
    print("{:-^30}".format("-"))
    
def all_symbol():
    for key, value in language.items():
        print(key, ':', value)
    
    
def pair_language():
    texts = input("Text to translate: ")
    destination = (input("Destination language: ")).lower()
    
    try:
        translate = translator.translate(texts, dest=destination)
        print("\a")
        print("Translated text:", translate.text)
    except:
        print("Language destination not exist")

def find_distance():
    print("-----Your Location------")
    location_la = float(input("Enter the latitude: "))
    location_lo = float(input("Enter the longitude: "))
    location = (location_la, location_lo)
    print("-----Your Destination-----")
    destination_la = float(input("Enter the latitude: "))
    destination_lo = float(input("Enter the longitude: "))
    destination = (destination_la,destination_lo)
    print("-----Destinace Between In Miles-----")
    print(geodesic(location,destination).miles)

def quick_facts(destination):
    country = CountryInfo(destination)
    data1 = country.alt_spellings()
    print(data1)
    data2 = country.capital()
    print(data2)
    data3 = country.currencies()
    print(data3)
    data4 = country.languages()
    print(data4)
    data5 = country.timezones()
    print(data5)
    data7 = country.borders()
    print(data7)

def currency_converter():
    c = CurrencyConverter()
    print("Exchange Your Currency")
    current = input("Current Currency: ")
    future = input("Expected Currency: ")
    amount = float(input("How much do you want to exchange? "))
    print(c.convert(amount, current, future))

#if __name__ == '__main__':
   #homepage()
   #titles()
   #menu()
homepage()
