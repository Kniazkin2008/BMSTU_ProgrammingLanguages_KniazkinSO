from random import uniform
from math import pi
import turtle as tr


# Проверка принадлежности точки области
def function(x, y, r):
    if (x <= 0 and 0 >= y >= -x - r) or (x >= 0 and y >= 0 and y**2 <= r**2 - x**2):
        return 1
    else:
        return 0


try:
    r = float(input("Введите r: "))

    if r <= 0:
        print("Радиус должен быть больше нуля.")
    else:
        Nmax = 10000
        Nf = 0

        # Настройка окна
        tr.setup(0.50, 0.65)
        tr.title("Метод Монте-Карло")

        width = tr.window_width()
        height = tr.window_height()

        # Вычисление масштаба
        scale_x = (width - 100) / (2 * r)
        scale_y = (height - 230) / (2 * r)

        if scale_x < scale_y:
            scale = scale_x
        else:
            scale = scale_y

        # Установка системы координат
        tr.setworldcoordinates(
            -width / (2 * scale),
            60 / scale - height / (2 * scale),
            width / (2 * scale),
            60 / scale + height / (2 * scale)
        )

        tr.hideturtle()
        tr.tracer(0)

        # Генерация случайных точек
        for i in range(Nmax):
            x = uniform(-r, r)
            y = uniform(-r, r)

            flag = function(x, y, r)

            if flag == 1:
                Nf += 1
                tr.color("green")
            else:
                tr.color("pink")

            tr.up()
            tr.goto(x, y)
            tr.dot(3)

            if i % 250 == 0:
                tr.update()

        # Построение координатных осей
        tr.color("blue")
        tr.pensize(2)

        tick = 5 / scale
        arrow = 8 / scale

        # Ось X
        tr.up()
        tr.goto(-r - 15 / scale, 0)
        tr.down()
        tr.goto(r + 15 / scale, 0)

        # Стрелка оси X
        for k in (-1, 1):
            tr.up()
            tr.goto(r + 15 / scale, 0)
            tr.down()
            tr.goto(r + 7 / scale, k * arrow / 2)

        # Ось Y
        tr.up()
        tr.goto(0, -r - 15 / scale)
        tr.down()
        tr.goto(0, r + 15 / scale)

        # Стрелка оси Y
        for k in (-1, 1):
            tr.up()
            tr.goto(0, r + 15 / scale)
            tr.down()
            tr.goto(k * arrow / 2, r + 7 / scale)

        tr.up()

        # Деления и подписи оси X
        for i in range(-2, 3):
            x = i * r / 2

            tr.goto(x, -tick)
            tr.down()
            tr.goto(x, tick)
            tr.up()

            tr.goto(x, -22 / scale)
            tr.write("{:.2f}".format(x), align="center")

        # Деления и подписи оси Y
        for i in range(-2, 3):
            y = i * r / 2

            if i != 0:
                tr.goto(-tick, y)
                tr.down()
                tr.goto(tick, y)
                tr.up()

                tr.goto(10 / scale, y - 5 / scale)
                tr.write("{:.2f}".format(y))

        # Названия осей
        tr.goto(r + 25 / scale, 5 / scale)
        tr.write("X", font=("Arial", 12, "bold"))

        tr.goto(10 / scale, r + 20 / scale)
        tr.write("Y", font=("Arial", 12, "bold"))

        # Вычисление площади
        Sf = 4 * r**2 * Nf / Nmax
        S = r**2 / 2 + pi * r**2 / 4
        Er = abs(Sf - S) / S * 100

        # Вывод результатов
        print("N =", Nmax)
        print("Nf =", Nf)
        print("Sf = {:.4f}".format(Sf))
        print("S = {:.4f}".format(S))
        print("Er = {:.2f}%".format(Er))

        # Заголовок
        top = 60 / scale + height / (2 * scale)

        tr.color("black")
        tr.up()
        tr.goto(0, top - 25 / scale)
        tr.write("Метод Монте-Карло",
                 align="center",
                 font=("Arial", 14, "bold"))

        # Результаты на рисунке
        tr.color("blue")

        tr.goto(0, top - 50 / scale)
        tr.write("N = {}".format(Nmax), align="center")

        tr.goto(0, top - 70 / scale)
        tr.write("Nf = {}".format(Nf), align="center")

        tr.goto(0, top - 90 / scale)
        tr.write("Sf = {:.4f}".format(Sf), align="center")

        tr.goto(0, top - 110 / scale)
        tr.write("S = {:.4f}".format(S), align="center")

        tr.goto(0, top - 130 / scale)
        tr.write("Er = {:.2f}%".format(Er), align="center")

        tr.update()
        tr.done()

except ValueError:
    print("Невозможно преобразовать входные данные.")