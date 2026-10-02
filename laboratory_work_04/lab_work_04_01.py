from random import uniform


try:
    n = int(input("Введите количество элементов массива: "))

    if n <= 0:
        print("Количество элементов должно быть больше нуля.")
    else:
        A = []

        for i in range(n):
            A.append(uniform(-10, 10))
        print("Исходный массив:")
        for i in range(n):
            print("{0:7.2f}".format(A[i]), end=" ")
        print()

        # 1. Номер минимального по модулю элемента
        min_index = 0
        for i in range(1, n):
            if abs(A[i]) < abs(A[min_index]):
                min_index = i
        print("Номер минимального по модулю элемента:", min_index + 1)

        # 2. Сумма модулей элементов после первого отрицательного
        first_neg = -1
        for i in range(n):
            if A[i] < 0:
                first_neg = i
                break
        summa = 0

        if first_neg != -1:
            for i in range(first_neg + 1, n):
                summa += abs(A[i])
            print("Сумма модулей элементов после первого отрицательного: {0:.2f}".format(summa))
        else:
            print("В массиве нет отрицательных элементов.")

        # 3. Сжатие массива
        a = float(input("Введите a: "))
        b = float(input("Введите b: "))
        if a > b:
            print("Значение a должно быть меньше или равно b.")
        else:
            j = 0
            for i in range(n):
                if A[i] < a or A[i] > b:
                    A[j] = A[i]
                    j += 1
            while j < n:
                A[j] = 0
                j += 1
            print("Массив после сжатия:")
            for i in range(n):
                print("{0:7.2f}".format(A[i]), end=" ")
            print()

except ValueError:
    print("Невозможно преобразовать входные данные.")