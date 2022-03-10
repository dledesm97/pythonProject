from countryinfo import CountryInfo

def quick_facts(destination):
    new_destination = destination
    country = CountryInfo(destination)
    print("{:-^100}".format("-"))
    nicknames = country.alt_spellings()
    print(f"Nicknames for {destination}: {nicknames}")
    capital = country.capital()
    print(f"\nThe capital of {destination} is {capital}")
    currency = country.currencies()
    print(f"\nThe currency in {destination} is {currency}")
    language = country.languages()
    print(f"\nThe official language in {destination} is {language}")
    timezones = country.timezones()
    print(f"\n{destination}'s timezone(s): {timezones}")
    borders = country.borders()
    print(f"\nCountries that surround {destination} are: {borders}")
    print("{:-^100}".format("-"))
