fi = open("lab4_pb_in.txt", "rt")
fo = open("lab4_pd_ou.txt", "wt")

line = fi.readline()
line = fi.readline()

n, a, b = fi.readline().split()

n = int(n)
a = float(a)
b = float(b)

A = []

for value in fi.readline().split():
    A.append(float(value))

if n <= 0 or len(A) != n:
    fo.write("Некорректное количество элементов массива.\n")
else:
    fo.write("Исходный массив:\n")

    for i in range(n):
        fo.write("{0:7.2f}".format(A[i]))
    fo.write("\n")

    # 1. Номер минимального по модулю элемента
    min_index = 0

    for i in range(1, n):
        if abs(A[i]) < abs(A[min_index]):
            min_index = i

    fo.write("Номер минимального по модулю элемента: {0}\n".format(min_index + 1))

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

        fo.write("Сумма модулей элементов после первого отрицательного: {0:.2f}\n".format(summa))
    else:
        fo.write("В массиве нет отрицательных элементов.\n")

    # 3. Сжатие массива
    if a > b:
        fo.write("Значение a должно быть меньше или равно b.\n")

    else:
        j = 0

        for i in range(n):
            if A[i] < a or A[i] > b:
                A[j] = A[i]
                j += 1

        while j < n:
            A[j] = 0
            j += 1

        fo.write("Массив после сжатия:\n")

        for i in range(n):
            fo.write("{0:7.2f}".format(A[i]))
        fo.write("\n")

fi.close()
fo.close()