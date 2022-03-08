from googletrans import Translator
import language
import os

language = language.LANGUAGES
translator = Translator()

def homepage():
    print("{:-^30}".format("-"))
    print("{:^30}".format("Where are you traveling?"))
    print("{:-^30}".format("-"))

    destination = input("Enter the location?")
    os.system('clear')

def titles():
    #os.system('clear')
    print("{:-^30}".format("-"))
    print("{:^30}".format("Simple Translation Program"))
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
            print("Thanks for using")
            exit()
        else:
            print("Choice not found")


if __name__ == '__main__':
    titles()
    menu()
