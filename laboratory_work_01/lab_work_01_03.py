from math import sin, tan


def function_1(alpha):
    z1 = (1 - 2 * sin(alpha)**2) / (1 + sin(2 * alpha))
    return z1


def function_2(alpha):
    z2 = (1 - tan(alpha)) / (1 + tan(alpha))
    return z2


if __name__ == "__main__":
    try:
        alpha = float(input("Введите alpha: "))

        z1 = function_1(alpha)
        print(f"Результат вычисления первой функции: {z1:.4f}")

        z2 = function_2(alpha)
        print(f"Результат вычисления второй функции: {z2:.4f}")

    except ValueError:
        print("Невозможно преобразовать входные данные.")

    except ZeroDivisionError:
        print("Ошибка: деление на ноль.")