from geopy.distance import geodesic
from countryinfo import CountryInfo
from currency_converter import CurrencyConverter
import translator
import os

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
        translator.menu()
    if userInput == 2:
        find_distance()
    if userInput == 3:
        quick_facts(destination)
    if userInput == 4:
        currency_converter()
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
