from colorama import Fore, Style


def bank_percents():
    rubles = float(input("Сколько денег вы кладете на вклад?: "))
    years = float(input("На сколько лет вы кладете деньги?: "))
    percents = float(input("Под какой процент?: "))

    for year in range(years):
        rubles *= 1 + (percents / 100)

    print(Fore.GREEN + f"Будет на счету: {str(round(rubles, 2))}" + Style.RESET_ALL)


if __name__ == "__main__":
    bank_percents()
