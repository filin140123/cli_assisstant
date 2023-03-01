from random import choice, randint
from colorama import Fore, Style
from string import ascii_lowercase, ascii_uppercase, digits

lowcase, uppercase, numbers = list(ascii_lowercase), list(ascii_uppercase), list(digits)
special = ["!", "@", "#", "$", "%", "&", "*", "(", ")", "?", "=", "+"]


def passgen():
    count = int(input("Сколько символов должно быть в пароле?: "))

    print(Fore.CYAN + "Новый сгенерированный пароль: " + Style.RESET_ALL, end="")

    for i in range(count):
        symbol_type = randint(1, 4)
        if symbol_type == 1:
            i = choice(lowcase)
        elif symbol_type == 2:
            i = choice(uppercase)
        elif symbol_type == 3:
            i = choice(numbers)
        elif symbol_type == 4:
            i = choice(special)
        print(i, end="")
    print()


if __name__ == "__main__":
    passgen()
