from googletrans import Translator
import language

translator = Translator()
language = language.LANGUAGES

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
