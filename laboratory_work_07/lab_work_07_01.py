from math import sqrt
import turtle as tr


def function(x):
    r = 1

    if -3 <= x < -2:
        return -x - 2
    elif -2 <= x < -1:
        return sqrt(r**2 - (x + 1)**2)
    elif -1 <= x < 1:
        return 1
    elif 1 <= x < 2:
        return 3 - 2 * x
    else:
        return -1


Xbeg = float(input("Введите Xнач: "))
Xend = float(input("Введите Xкон: "))

if Xbeg < -3 or Xend > 5 or Xbeg >= Xend:
    print("Введите корректный диапазон от -3 до 5")
else:
    Nmax = 300
    dx = (Xend - Xbeg) / Nmax

    # Настройка окна
    tr.setup(0.55, 0.45)
    tr.title("График функции")
    tr.hideturtle()
    tr.tracer(0)

    width = tr.window_width()
    height = tr.window_height()

    # Границы оси X
    if Xbeg < 0:
        left = Xbeg - 0.5
    else:
        left = -0.5

    if Xend > 0:
        right = Xend + 0.5
    else:
        right = 0.5

    # Поиск минимального и максимального Y
    ymin = function(Xbeg)
    ymax = function(Xbeg)

    if ymin > 0:
        ymin = 0

    if ymax < 0:
        ymax = 0

    for i in range(Nmax + 1):
        xt = Xbeg + i * dx
        y = function(xt)

        if y < ymin:
            ymin = y

        if y > ymax:
            ymax = y

    bottom = ymin - 0.5
    top = ymax + 0.5

    # Вычисление масштаба
    scale_x = (width - 120) / (right - left)
    scale_y = (height - 160) / (top - bottom)

    if scale_x < scale_y:
        scale = scale_x
    else:
        scale = scale_y

    xc = (left + right) / 2
    yc = (bottom + top) / 2

    tr.setworldcoordinates(
        xc - width / (2 * scale),
        yc - height / (2 * scale),
        xc + width / (2 * scale),
        yc + height / (2 * scale)
    )

    window_top = yc + height / (2 * scale)

    tick = 5 / scale
    arrow = 8 / scale

    # Построение осей
    tr.color("blue")
    tr.pensize(2)

    # Ось X
    tr.up()
    tr.goto(left, 0)
    tr.down()
    tr.goto(right, 0)

    # Стрелка оси X
    for k in (-1, 1):
        tr.up()
        tr.goto(right, 0)
        tr.down()
        tr.goto(right - arrow, k * arrow / 2)

    # Ось Y
    tr.up()
    tr.goto(0, bottom)
    tr.down()
    tr.goto(0, top)

    # Стрелка оси Y
    for k in (-1, 1):
        tr.up()
        tr.goto(0, top)
        tr.down()
        tr.goto(k * arrow / 2, top - arrow)

    # Деления и подписи оси X
    for x in range(-3, 6):
        if left < x < right:
            tr.up()
            tr.goto(x, -tick)
            tr.down()
            tr.goto(x, tick)

            tr.up()
            if x == 0:
                tr.goto(-0.15, -0.25)
            else:
                tr.goto(x, -0.25)

            tr.write(str(x), align="center")

    # Деления и подписи оси Y
    for y in range(-1, 2):
        if bottom < y < top and y != 0:
            tr.up()
            tr.goto(-tick, y)
            tr.down()
            tr.goto(tick, y)

            tr.up()
            tr.goto(0.15, y - 0.05)
            tr.write(str(y))

    # Подписи осей
    tr.up()
    tr.goto(right + 0.1, 0.1)
    tr.write("X", font=("Arial", 12, "bold"))

    tr.goto(0.15, top + 0.05)
    tr.write("Y", font=("Arial", 12, "bold"))

    # Заголовок
    tr.goto(xc, window_top - 25 / scale)
    tr.write("График функции", align="center",
             font=("Arial", 12, "bold"))

    tr.update()

    # Построение графика
    tr.color("green")
    tr.pensize(2)
    tr.speed(10)
    tr.hideturtle()
    tr.tracer(1)

    tr.up()
    tr.goto(Xbeg, function(Xbeg))
    tr.down()

    for i in range(1, Nmax + 1):
        xt = Xbeg + i * dx
        tr.goto(xt, function(xt))

    tr.up()
    tr.hideturtle()
    tr.done()