from math import sqrt


try:
    Xbeg = float(input("Введите Xнач: "))
    Xend = float(input("Введите Xкон: "))
    dx = float(input("Введите шаг dx: "))
    r = 1

    if Xbeg < -3 or Xend > 5:
        print("Введите значения в диапозоне от -3 до 5")
    elif Xbeg > Xend:
        print("Введите корректные данные. Xbeg должен быть меньше Xend")
    elif dx <= 0:
        print("Шаг dx должен быть больше нуля.")
    else:
        print(f"Xbeg = {Xbeg:.2f}   Xend = {Xend:.2f}")
        print(f"Dx= {dx:.2f}")
        print("+--------+--------+")
        print("I    X   I    Y   I")
        print("+--------+--------+")

        xt = Xbeg
        while xt <= Xend:
            if -3 <= xt < -2:
                y = -xt - 2
            elif -2 <= xt < -1:
                y = sqrt(r**2 - (xt + 1)**2)
            elif -1 <= xt < 1:
                y = 1
            elif 1 <= xt < 2:
                y = 3 - 2 * xt
            elif 2 <= xt <= 5:
                y = -1
            print("I {0:6.2f} I {1:6.2f} I".format(xt, y))

            xt += dx

        print("+--------+--------+")

except ValueError:
    print("Нужно вводить только числа!")