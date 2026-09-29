from random import uniform


try:
    r = float(input("Введите r: "))

    if r < 0:
        print("Радиус не может быть отрицательным.")
    else:
        print("{:>8} {:>8} {:>5}".format("X", "Y", "Res"))
        print("-" * 25)

        for i in range(10):
            x = uniform(-r, r)
            y = uniform(-r, r)

            if (x <= 0 and 0 >= y >= -x - r) or (x >= 0 and y >= 0 and y ** 2 <= r ** 2 - x ** 2):
                flag = 1
            else:
                flag = 0

            if flag == 1:
                print("{:8.2f} {:8.2f} {:>5}".format(x, y, "Yes"))
            else:
                print("{:8.2f} {:8.2f} {:>5}".format(x, y, "No"))

except ValueError:
    print("Невозможно преобразовать входные данные.")