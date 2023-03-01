from colorama import Fore, Style


def calculate():
    formula = input("Введите пример: ")
    x = eval(formula)
    print(f"{formula} = " + Fore.GREEN + f"{x}" + Style.RESET_ALL)


if __name__ == "__main__":
    calculate()
