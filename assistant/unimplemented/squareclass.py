class CalcSquare:
    def __init__(self):
        pass

    def perimeter(self, side):
        p = side * 4
        if p % 1 == 0:
            p = int(p)
        return p

    def area(self, side):
        a = side ** 2
        if a % 1 == 0:
            a = int(a)
        return a

    def diagonal(self, side):
        d = round(side * (2 ** 0.5), 2)
        if d % 1 == 0:
            d = int(d)
        return d

    def all_info(self, side):
        cs = CalcSquare()
        return f"p = {cs.perimeter(side)}, s = {cs.area(side)}, d = {cs.diagonal(side)}"


cs = CalcSquare()

x = float(input("Введите сторону квадрата: "))

print(
    "Что вы хотите узнать?\n"
    "1. Периметр\n"
    "2. Площадь\n"
    "3. Диагональ\n"
    "4. Все сразу\n"
)

option = input(">>> ")

if option == "1":
    print(cs.perimeter(x))
elif option == "2":
    print(cs.area(x))
elif option == "3":
    print(cs.diagonal(x))
elif option == "4":
    print(cs.all_info(x))
else:
    print("Что-то пошло не так...")
