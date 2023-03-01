from colorama import Fore, Style
import pickle


def controls():
    print("\nВот что я могу: ")
    print(
        " --> Узнать погоду\n"
        " --> Поставить таймер\n"
        " --> Калькулятор\n"
        " --> Посчитать проценты на вклад\n"
        " --> Сгенерировать сложный пароль\n"
        " --> Переводчик\n"
        ' --> Игра "Угадай число"\n'
        " --> Выйти из программы\n"
    )


def rename(u):
    print(Fore.CYAN, end="")
    u["username"] = input("Как вас зовут?: ")
    print(Style.RESET_ALL, end="")
    # saving
    with open("savefile.dat", "wb") as f:
        pickle.dump(u, f, protocol=2)


if __name__ == "__main__":
    controls()
    rename(u)
