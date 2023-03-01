import re

# список с исключениями
exceptions = [
    "а",
    "и",
    "о",
    "у",
    "от",
    "или",
    "что",
    "в",
    "это",
    "не",
    "на",
    "с",
    "за",
    "по",
    "то",
    "из",
    "но",
    "к",
    "как",
    "так",
    "же",
    "он",
    "его",
    "ты",
    "я",
    "все",
    "она",
    "они",
    "когда",
    "мы",
    "тебя",
    "под",
    "да",
    "был",
    "ну",
    "тебе",
    "для",
    "мне",
    "кто",
    "бы",
    "их",
    "через",
    "здесь",
    "него",
    "ли",
    "этот",
    "теперь",
    "были",
    "ни",
    "чем",
    "тот",
    "раз",
    "может",
    "есть",
    "эту",
    "при",
    "ей",
    "эти",
    "которых",
]

# спрашиваем у пользователя имя файла
print("Название файла с разрешением (пример: sample.txt)")
a = input("Файл должен находится в одной папке со скриптом: ")
b = input("Кодировка: 1. utf-8, 2. windows-1251: ")
if b == "2":
    code = "windows-1251"
else:
    code = "utf-8"
c = input(
    "Использовать словарь исключений? (союзы, предлоги, местоимения...)\n"
    "1. Да, 2. Нет: "
    )
d = int(input("Топ из скольких слов вы хотите узнать?: "))

# открываем, читаем файл и заменяем все переносы пустотой
with open(a, "r", encoding=code) as file:
    text_sample = file.read().replace("\n", " ")

# убираем знаки препинания и переводим текст в лоуеркейс, получаем список слов
text_sample = re.findall(r"[\w']+", text_sample.lower())

# получаем словарь, где ключ — количество упоминаний слова, а значение — само слово
countlist = []
for i in text_sample:
    countlist.append([text_sample.count(i), i])
m = dict(countlist)

# чистим словарь на исключения
if c != "2":
    m = {key: val for key, val in m.items() if val not in exceptions}

# вычисляем самое частое слово
most_common = m[max(m.keys())]

# вычисляем топ-10 самых частых слов
m = sorted(m.items())[-d:][::-1]

# вычисляем самое длинное слово
longest_word = max(text_sample, key=len)

# печатаем данные в оригинальный файл
with open(a, "a", encoding=code) as file:
    print("\n", file=file)
    print(f"Наиболее частое слово: {most_common}", file=file)
    print(f"Наиболее длинное слово: {longest_word}", file=file)
    print(f"Всего слов: {len(countlist)}", file=file)
    print(f"\nТоп {d} слов:", file=file)
    for k, v in m:
        print(f"{v} — {k} упоминание(я, й)", file=file)

print("\n", file=file)
print(f"Наиболее частое слово: {most_common}", file=file)
print(f"Наиболее длинное слово: {longest_word}", file=file)
print(f"Всего слов: {len(countlist)}", file=file)
print(f"\nТоп {d} слов:", file=file)
for k, v in m:
    print(f"{v} — {k} упоминание(я, й)", file=file)
