from googletrans import Translator
import language

#creating an instance from Translator() that we imported from googleterans
translator = Translator()
#accessing the Languages list from the language.py file
language = language.LANGUAGES

def menu():
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
            pair_language()
        elif choose == "2":
            language_title()
            all_symbol()
        elif choose == "3":
            print("Have a good day!")
            exit()
        else:
            print("Choice not found")

def language_title():
    print("{:-^30}".format("-"))
    print("{:^30}".format("Available Languages"))
    print("{:-^30}".format("-"))

def all_symbol():
    for key, value in language.items(): #listing out all the available languages for translation
        print(key, ':', value)


def pair_language():
    #os.system('clear')
    print("{:-^30}".format("-"))
    print("{:^30}".format("Let me help you translate"))
    print("{:-^30}".format("-"))
    texts = input("Text to translate: ")
    destination = (input("Destination language: ")).lower() #in order to correctly pair the language the symbol must be lowercase

    try:
        translate = translator.translate(texts, dest=destination)
        print("\a")
        print("Translated text:", translate.text)
    except:
        print("Language destination not exist")
