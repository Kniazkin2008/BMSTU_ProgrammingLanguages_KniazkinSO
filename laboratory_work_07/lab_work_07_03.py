import turtle as tr


# Вычисление суммы ряда
def function(x):
    eps = 0.001
    n = 0
    y = 0

    while True:
        an = 1 / ((2 * n + 1) * x ** (2 * n + 1))

        if abs(an) < eps:
            break

        y += an
        n += 1

    return y


try:
    Xbeg = float(input("Введите Xнач: "))
    Xend = float(input("Введите Xкон: "))

    if Xbeg >= Xend:
        print("Введите корректные данные.")
    elif Xbeg <= 1 and Xend >= -1:
        print("Значения x должны удовлетворять условию |x| > 1.")
    else:
        Nmax = 300
        dx = (Xend - Xbeg) / Nmax

        # Определение границ графика
        ymin = 0
        ymax = 0

        for i in range(Nmax + 1):
            xt = Xbeg + i * dx
            y = function(xt)

            if y < ymin:
                ymin = y

            if y > ymax:
                ymax = y

        # Настройка окна
        tr.setup(0.60, 0.60)
        tr.title("График суммы ряда")

        width = tr.window_width()
        height = tr.window_height()

        # Масштабирование
        scale_x = (width - 140) / (Xend - Xbeg)
        scale_y = (height - 115) / (ymax - ymin)

        # Границы системы координат
        if Xbeg > 1:
            left = Xbeg - 85 / scale_x
            right = Xend + 55 / scale_x
            axis_x = Xbeg - 50 / scale_x
        else:
            left = Xbeg - 45 / scale_x
            right = Xend + 95 / scale_x
            axis_x = Xend + 45 / scale_x

        bottom = ymin - 45 / scale_y
        top = ymax + 70 / scale_y

        tr.setworldcoordinates(left, bottom, right, top)

        tr.hideturtle()
        tr.tracer(0)

        # Размеры делений и стрелок
        tick_x = 5 / scale_x
        tick_y = 5 / scale_y

        tr.color("blue")
        tr.pensize(2)

        # Ось X
        tr.up()
        tr.goto(left + 15 / scale_x, 0)
        tr.down()
        tr.goto(right - 15 / scale_x, 0)

        # Стрелка X
        for k in (-1, 1):
            tr.up()
            tr.goto(right - 15 / scale_x, 0)
            tr.down()
            tr.goto(right - 23 / scale_x,
                    k * 4 / scale_y)

        # Ось Y
        tr.up()
        tr.goto(axis_x, ymin - 20 / scale_y)
        tr.down()
        tr.goto(axis_x, ymax + 20 / scale_y)

        # Стрелка Y
        for k in (-1, 1):
            tr.up()
            tr.goto(axis_x, ymax + 20 / scale_y)
            tr.down()
            tr.goto(axis_x + k * 4 / scale_x,
                    ymax + 12 / scale_y)

        tr.up()

        # Деления и подписи оси X
        for i in range(6):
            xt = Xbeg + i * (Xend - Xbeg) / 5

            tr.goto(xt, -tick_y)
            tr.down()
            tr.goto(xt, tick_y)
            tr.up()

            tr.goto(xt, -22 / scale_y)
            tr.write("{:.2f}".format(xt), align="center")

        # Деления и подписи оси Y
        for i in range(5):
            y = ymin + i * (ymax - ymin) / 4

            tr.goto(axis_x - tick_x, y)
            tr.down()
            tr.goto(axis_x + tick_x, y)
            tr.up()

            if Xbeg > 1:
                tr.goto(axis_x - 9 / scale_x,
                        y - 5 / scale_y)
                tr.write("{:.2f}".format(y), align="right")
            else:
                tr.goto(axis_x + 9 / scale_x,
                        y - 5 / scale_y)
                tr.write("{:.2f}".format(y))

        # Названия осей
        tr.goto(right - 12 / scale_x, 12 / scale_y)
        tr.write("X", font=("Arial", 12, "bold"))

        tr.goto(axis_x + 10 / scale_x,
                ymax + 32 / scale_y)
        tr.write("Y", font=("Arial", 12, "bold"))

        # Заголовок
        tr.color("black")
        tr.goto((left + right) / 2, top - 25 / scale_y)
        tr.write("График суммы ряда",
                 align="center",
                 font=("Arial", 14, "bold"))

        # Построение графика
        tr.color("green")
        tr.pensize(3)

        for i in range(Nmax + 1):
            xt = Xbeg + i * dx
            y = function(xt)

            if i == 0:
                tr.up()
                tr.goto(xt, y)
                tr.down()
            else:
                tr.goto(xt, y)

            if i % 10 == 0:
                tr.update()

        tr.up()
        tr.update()
        tr.done()

except ValueError:
    print("Невозможно преобразовать входные данные.")