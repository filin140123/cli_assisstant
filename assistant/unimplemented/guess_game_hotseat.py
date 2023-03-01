from random import randint

number = randint(1, 100)
guess = None
count = 0

levels = {
    1: 10, 
    2: 8, 
    3: 6,
    4: 4,
    5: 3
}

level = int(input(f"Выберите уровень сложности {[*levels]}: "))
max_count = levels[level]

user_count = int(input("Введите количество пользователей: "))
users = []

for user in range(user_count):
    user_name = input(f"Введите имя пользователя {user}: ")
    users.append(user_name)

print("\nИгроки: ", end='')
for u in users: print(u, end=', ')
print("приготовьтесь!\n")

is_winner = False
winner_name = None

while not is_winner:

    count += 1
    if count > max_count:
        print("Все пользователи проиграли")
        break

    if count == max_count: print("Последняя попытка!")
    else: print(f"Попытка {count} из {max_count}")

    for user in users:
        print(f"Ход пользователя {user}")

        guess = int(input("Введите число: "))
        if guess == number:
            is_winner = True
            winner_name = user
            break

        if guess > number: print("Ваше число больше загаданного\n")
        elif guess < number: print("Ваше число меньше загаданного\n")

else: print(f"Победитель — {winner_name}. Вы угадали число!")

input("Нажмите любую клавишу для выхода...")