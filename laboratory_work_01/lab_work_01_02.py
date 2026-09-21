from math import sin, tan


try:

    alpha = float(input("Введите alpha: "))

    z1 = (1 - 2 * (sin(alpha)**2))/(1 + sin(2 * alpha))

    print(f"Результат вычисления функции:  {z1:.4f}")

    z2 = (1 - tan(alpha)) / (1 + tan(alpha))

    print(f"Результат вычисления функции: {z2:.4f}")

except ValueError:
    print("Не возможно преобразовать входные данные.")

except ZeroDivisionError:
    print("Ошибка: деление на ноль.")
