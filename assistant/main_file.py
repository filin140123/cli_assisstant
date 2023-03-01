from colorama import Fore, Back, Style, init
from playsound import playsound
from weather import get_weather
from controls import controls, rename
from timer import timer
from bank import bank_percents
from passgen import passgen
from calceval import calculate
from guess_game import guess_game
from translator import translator
import pickle

init()

user = {
    "username": "",
}

# loading
try:
    with open("savefile.dat", "rb") as f:
        user = pickle.load(f)
except FileNotFoundError:
    pass

while user["username"] == "":
    rename(user)


print(f"Привет, {user['username']}!")


while True:
    playsound("sound83.wav")
    controls()
    action = input(f"Чем могу еще помочь, {user['username']}?: ")

    act_list = action.lower().split(" ")
    if "погода" in act_list:
        get_weather()
        continue
    elif "таймер" in act_list:
        timer()
        continue
    elif "калькулятор" in act_list:
        calculate()
        continue
    elif "перевод" in act_list:
        translator()
        continue
    elif "банк" in act_list:
        bank_percents()
        continue
    elif "пароль" in act_list:
        passgen()
        continue
    elif "угадай" in act_list:
        guess_game()
        continue
    elif "имя" in act_list:
        rename(user)
        continue
    elif "выход" in act_list:
        print(f"Пока, {user['username']}!")
        break
