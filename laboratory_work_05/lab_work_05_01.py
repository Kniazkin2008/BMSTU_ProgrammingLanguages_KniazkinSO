from random import uniform


n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
value = float(input("Введите заданную величину: "))

def create_matr(n, m):
    matr = []

    for i in range(n):
        matr.append([])
        for j in range(m):
            matr[i].append(uniform(-10, 10))

    return matr

matr = create_matr(n, m)

def print_matr(matr):
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            print("{0:8.2f}".format(matr[i][j]), end=" ")
        print()

print("Исходная матрица:")
print_matr(matr)

def triangle_matr(matr):
    n = len(matr)
    m = len(matr[0])
    k = 0

    for j in range(m):
        if k >= n:
            break

        if matr[k][j] == 0:
            for i in range(k + 1, n):
                if matr[i][j] != 0:
                    matr[k], matr[i] = matr[i], matr[k]
                    break

        if matr[k][j] != 0:
            for i in range(k + 1, n):
                coef = matr[i][j] / matr[k][j]

                for p in range(j + 1, m):
                    matr[i][p] -= coef * matr[k][p]
                matr[i][j] = 0.0
            k += 1

    return matr

matr = triangle_matr(matr)

print("Матрица треугольного вида:")
print_matr(matr)

def count_rows(matr, value):
    count = 0

    for i in range(len(matr)):
        summa = 0

        for j in range(len(matr[i])):
            summa += matr[i][j]
        average = summa / len(matr[i])
        print("Среднее арифметическое строки {0}: {1:.2f}".format(i + 1, average))

        if average < value:
            count += 1
    return count

count = count_rows(matr, value)

print("Количество строк со средним меньше заданной величины:", count)
