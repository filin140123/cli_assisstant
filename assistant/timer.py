import time
import datetime
from colorama import Fore, Style


def counter(m, s):

    s += m * 60

    try:
        while s > 0:
            display = datetime.timedelta(seconds=s)
            print(display, end="\r")
            time.sleep(1)
            s -= 1

        print("0:00:00")
        print("Время вышло :)")

    except KeyboardInterrupt:
        print("Таймер прерван :(")


def timer():
    user_time = input(
        "На сколько минут/секунд нужен таймер? (разделите числа пробелами): "
    )
    print(Fore.RED + "Ctrl+C чтобы прервать таймер..." + Style.RESET_ALL)
    spl_time = user_time.split(" ")
    if len(spl_time) == 2:
        counter(int(spl_time[0]), int(spl_time[1]))
    else:
        counter(0, int(spl_time[0]))


if __name__ == "__main__":
    timer()
