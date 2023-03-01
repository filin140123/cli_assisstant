from random import randint
from playsound import playsound


def guess_game():
    number = randint(1, 100)
    guess = None
    count = 0

    levels = {1: 10, 2: 7, 3: 5}

    level = int(input(f"Выберите уровень сложности {[*levels]}: "))
    max_count = levels[level]

    while number != guess:

        count += 1
        if count > max_count:
            print("Вы проиграли")
            break

        if count == max_count:
            print("Последняя попытка!")
        else:
            print(f"Попытка {count} из {max_count}")

        guess = int(input("Введите число: "))

        if guess > number:
            print("Ваше число больше загаданного")
        elif guess < number:
            print("Ваше число меньше загаданного")

    else:
        print("Вы угадали!")
        playsound("game_win.wav")


if __name__ == "__main__":
    guess_game()
