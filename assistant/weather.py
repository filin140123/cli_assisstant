from requests import get


def get_weather():
    city = input("Какой город? (Нажмите Enter для авто-определения): ")

    how_far = input("1. Погода сейчас\n2. Прогноз на 3 дня\n")

    if how_far == "2":
        mod = ""
    else:
        mod = "?0&"

    url = f"http://wttr.in/{city}{mod}?T&lang=ru"
    results = get(url)

    print(results.text)


if __name__ == "__main__":
    get_weather()
