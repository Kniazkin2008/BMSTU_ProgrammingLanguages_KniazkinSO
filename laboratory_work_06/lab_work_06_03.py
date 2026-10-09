fi = open("lab5_pb_in.txt", "rt")
fo = open("lab5_pd_ou.txt", "wt")

line = fi.readline()
line = fi.readline()

n, m, value = fi.readline().split()

n = int(n)
m = int(m)
value = float(value)


def create_matr(n, m):
    matr = []

    for i in range(n):
        row = []

        for number in fi.readline().split():
            row.append(float(number))

        matr.append(row)

    return matr


matr = create_matr(n, m)


def print_matr(matr):
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            fo.write("{0:8.2f}".format(matr[i][j]))
        fo.write("\n")


fo.write("Исходная матрица:\n")
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

fo.write("Матрица треугольного вида:\n")
print_matr(matr)


def count_rows(matr, value):
    count = 0

    for i in range(len(matr)):
        summa = 0

        for j in range(len(matr[i])):
            summa += matr[i][j]

        average = summa / len(matr[i])

        fo.write("Среднее арифметическое строки {0}: {1:.2f}\n".format(i + 1, average))

        if average < value:
            count += 1

    return count


count = count_rows(matr, value)

fo.write("Количество строк со средним меньше заданной величины: {0}\n".format(count))

fi.close()
fo.close()