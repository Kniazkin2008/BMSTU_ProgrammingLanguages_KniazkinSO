from math import sqrt


try:
    x = float(input("Введите значение аргумента: "))
    r = 1

    if x < -3 or x > 5:
        print("Введите значение в диапазоне от -3 до 5")
    else:
        if -3 <= x < -2:
            y = -x - 2
        elif -2 <= x < -1:
            y = sqrt(r**2 - (x + 1)**2)
        elif -1 <= x < 1:
            y = 1
        elif 1 <= x < 2:
            y = -2*x + 3
        elif 2 <= x <= 5:
            y = -1
        print("x= {0:.2f}    y= {1:.2f}".format(x,y))

except ValueError:
    print("Невозможно преобразовать входные данные.")
