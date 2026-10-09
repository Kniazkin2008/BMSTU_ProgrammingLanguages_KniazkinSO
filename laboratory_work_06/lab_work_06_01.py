from laboratory_work_01.lab_work_01_03 import function_1, function_2


if __name__ == "__main__":
    fi = open("lab1_pb_in.txt", "rt")
    fo = open("lab1_pd_ou.txt", "wt")

    line = fi.readline()
    line = fi.readline()

    fo.write("+----------+------------+------------+\n")
    fo.write("|  alpha   |     z1     |     z2     |\n")
    fo.write("+----------+------------+------------+\n")

    for line in fi:
        if line == "\n":
            continue

        try:
            alpha = float(line)

            z1 = function_1(alpha)
            z2 = function_2(alpha)

            fo.write("| {0:8.2f} | {1:10.4f} | {2:10.4f} |\n".format(alpha, z1, z2))

        except ValueError:
            fo.write("Невозможно преобразовать входные данные.\n")

        except ZeroDivisionError:
            fo.write("Ошибка: деление на ноль.\n")

    fo.write("+----------+------------+------------+\n")

    fi.close()
    fo.close()