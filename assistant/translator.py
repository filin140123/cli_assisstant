from translate import Translator as tl
from colorama import Fore, Style


def translator():
    x = input("1. ENG -> RUS, 2. RUS -> ENG: ")
    word = input("Что перевести?: ")

    if x == "2":
        translator = tl(from_lang="russian", to_lang="english")
    else:
        translator = tl(from_lang="english", to_lang="russian")

    result = translator.translate(word)
    print(Fore.CYAN + "Перевод: " + Style.RESET_ALL + f"{result}")


if __name__ == "__main__":
    translator()
