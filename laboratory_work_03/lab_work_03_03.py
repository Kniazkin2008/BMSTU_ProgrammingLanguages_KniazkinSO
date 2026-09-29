try:
    Xbeg = float(input("Введите Xнач: "))
    Xend = float(input("Введите Xкон: "))
    dx = float(input("Введите шаг dx: "))
    eps = float(input("Введите точность eps: "))

    if Xbeg > Xend or dx <= 0 or eps <= 0:
        print("Введите корректные данные.")
    elif Xbeg <= 1 and Xend >= -1:
        print("Значения x должны удовлетворять условию |x| > 1.")
    else:
        print(f"Xbeg = {Xbeg:.2f}   Xend = {Xend:.2f}")
        print(f"Dx = {dx:.2f}   Eps = {eps:.5f}")
        print("+--------+----------+-----+")
        print("I    X   I     Y    I  N  I")
        print("+--------+----------+-----+")

        xt = Xbeg

        while xt <= Xend:
            n = 0
            y = 0

            while True:
                an = 1 / ((2 * n + 1) * xt ** (2 * n + 1))

                if abs(an) < eps:
                    break

                y += an
                n += 1

            print("I {0:6.2f} I {1:8.3f} I {2:3d} I".format(xt, y, n))

            xt += dx

        print("+--------+----------+-----+")

except ValueError:
    print("Невозможно преобразовать входные данные.")