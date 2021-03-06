from countryinfo import CountryInfo

def quick_facts(destination):

    new_destination = destination
    country = CountryInfo(destination)
    print("{:-^100}".format("-"))
    nicknames = country.alt_spellings()
    print(f"Nicknames for {destination}: ")
    print(', '.join(nicknames))
    capital = country.capital()
    print(f"\nThe capital of {destination}: ")
    print(''.join(capital))
    currency = country.currencies()
    print(f"\nThe currency in {destination}: ")
    print(', '.join(currency))
    language = country.languages()
    print(f"\nThe official language in {destination}: ")
    print(''.join(language))
    timezones = country.timezones()
    print(f"\n{destination}'s timezone(s):")
    print (', '.join(timezones))
    borders = country.borders()
    print(f"\nCountries that surround {destination} are:")
    print (', '.join(borders))
    print("{:-^100}".format("-"))

    
