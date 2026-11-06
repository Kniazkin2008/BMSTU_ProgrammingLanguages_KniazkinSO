from tkinter import *
from tkinter.messagebox import showwarning, askyesno
from math import log, ceil, isfinite


def First(x, eps):
    # Первая функция через ряд
    t = (x - 1) / (x + 1)
    a = t
    Sum = 0
    n = 0
    q = 1 - t * t

    if q <= 0:
        raise ValueError("Не удалось вычислить ряд при таком Xmin или Xmax")

    while 2 * abs(a) / q > eps:
        Sum += a
        n += 1
        a *= t * t * (2 * n - 1) / (2 * n + 1)
        if n > 100000:
            raise ValueError("Ряд сходится слишком медленно. Измените интервал или eps")

    return 2 * Sum


def Second(x, b):
    # Вторая функция
    return log(x) + b


def GetData():
    # Получение данных из полей ввода
    try:
        xmin = float(ent2.get())
        xmax = float(ent3.get())
        dx = float(ent4.get())
        eps = float(ent5.get())
        b = float(ent6.get())
        marks = float(ent7.get())
    except ValueError:
        showwarning("Ошибка", "Введите числовые значения во все поля")
        return None

    if not all(isfinite(v) for v in (xmin, xmax, dx, eps, b, marks)):
        showwarning("Ошибка", "Все значения должны быть конечными числами")
        return None

    if xmin <= 0 or xmax <= xmin or dx <= 0 or eps <= 0 or marks <= 0:
        showwarning("Ошибка", "Должно быть: 0 < Xmin < Xmax, dx > 0, eps > 0, шаг меток > 0")
        return None

    return xmin, xmax, dx, eps, b, marks


def SetMark(x, y, axis):
    # Нанесение делений на оси
    if axis == "X":
        cv.create_line(x, Bottom, x, Bottom + 5, fill="black")
    else:
        cv.create_line(Left - 5, y, Left, y, fill="black")


def plotXY(xmin, xmax, ymin, ymax, marks):
    # Рисование осей и подписей
    cv.create_rectangle(Left, Top, Right, Bottom, outline="black")
    cv.create_text(MaxX / 2, 16, text="Графики функций. Вариант 11",
                   font=("Ubuntu", 12, "bold"))
    cv.create_text(MaxX / 2, 39, text="Синий: ряд     Красный: ln(x) + b",
                   font=("Ubuntu", 10))
    cv.create_text(Right + 12, Bottom, text="X")
    cv.create_text(Left, Top - 12, text="Y")

    # Деления с заданным шагом
    i = ceil(xmin / marks)
    while i * marks <= xmax:
        x = i * marks
        px = Left + (x - xmin) * Kx
        SetMark(px, Bottom, "X")
        cv.create_text(px, Bottom + 17, text=f"{x:.2f}", font=("Ubuntu", 9))
        i += 1

    i = ceil(ymin / marks)
    while i * marks <= ymax:
        y = i * marks
        py = Bottom - (y - ymin) * Ky
        SetMark(Left, py, "Y")
        cv.create_text(Left - 8, py, text=f"{y:.2f}", anchor=E,
                       font=("Ubuntu", 9))
        i += 1

    if ymin < 0 < ymax:
        py = Bottom - (0 - ymin) * Ky
        cv.create_line(Left, py, Right, py, fill="gray", dash=(3, 5))


def Fdraw(points, color, xmin, ymin):
    # Перевод координат в пиксели и рисование графика
    line = []
    for x, y in points:
        px = Left + (x - xmin) * Kx
        py = Bottom - (y - ymin) * Ky
        line.append((px, py))
    cv.create_line(line, fill=color, width=2)


def Draw():
    # Построение двух графиков
    global Xmin, Xmax, Ymin, Ymax, Kx, Ky
    data = GetData()
    if data is None:
        return

    xmin, xmax, dx, eps, b, marks = data

    # Проверка количества точек
    if (xmax - xmin) / dx > 10000:
        showwarning("Ошибка", "Слишком маленький dx для этого интервала")
        return

    first_points = []
    second_points = []
    try:
        i = 0
        while xmin + i * dx < xmax:
            x = xmin + i * dx
            y = First(x, eps)
            z = Second(x, b)
            first_points.append((x, y))
            second_points.append((x, z))
            i += 1

        # Добавляю правую границу интервала
        first_points.append((xmax, First(xmax, eps)))
        second_points.append((xmax, Second(xmax, b)))
    except ValueError as error:
        showwarning("Ошибка вычисления", str(error))
        return

    all_y = [p[1] for p in first_points] + [p[1] for p in second_points]
    ymin = min(all_y)
    ymax = max(all_y)
    margin = (ymax - ymin) * 0.1
    if margin == 0:
        margin = 1
    ymin -= margin
    ymax += margin

    # Чтобы не было  слишком большого количества делений
    if (xmax - xmin) / marks > 1000 or (ymax - ymin) / marks > 1000:
        showwarning("Ошибка", "Слишком маленький шаг меток для этого интервала")
        return

    Xmin, Xmax, Ymin, Ymax = xmin, xmax, ymin, ymax
    Kx = (Right - Left) / (Xmax - Xmin)
    Ky = (Bottom - Top) / (Ymax - Ymin)

    cv.delete("all")
    plotXY(Xmin, Xmax, Ymin, Ymax, marks)
    Fdraw(first_points, "blue", Xmin, Ymin)
    Fdraw(second_points, "red", Xmin, Ymin)


def showXY(event):
    # Координаты точки при щелчке мышью
    if Kx == 0 or Ky == 0:
        return
    if not (Left <= event.x <= Right and Top <= event.y <= Bottom):
        return

    x = Xmin + (event.x - Left) / Kx
    y = Ymin + (Bottom - event.y) / Ky
    ent0.delete(0, END)
    ent0.insert(0, f"{x:.2f}")
    ent1.delete(0, END)
    ent1.insert(0, f"{y:.2f}")

    cv.delete("cursor")
    cv.create_line(event.x, Top, event.x, Bottom, dash=(3, 5), tags="cursor")
    cv.create_line(Left, event.y, Right, event.y, dash=(3, 5), tags="cursor")


def window_deleted():
    # Завершение работы
    if askyesno("Выход", "Завершить работу?"):
        root.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("Лабораторная работа № 8. Вариант 11")
    root.resizable(False, False)
    root.protocol("WM_DELETE_WINDOW", window_deleted)

    MaxX = int(root.winfo_screenwidth() * 0.85)
    MaxY = int(root.winfo_screenheight() * 0.65)
    Left = 65
    Right = MaxX - 25
    Top = 60
    Bottom = MaxY - 45
    Kx = 0
    Ky = 0

    cv = Canvas(root, width=MaxX, height=MaxY, bg="white")
    cv.grid(row=0, column=0, columnspan=10)
    cv.bind("<Button-1>", showXY)

    Label(root, text="Xmin:").grid(row=1, column=0)
    ent2 = Entry(root, width=8)
    ent2.grid(row=1, column=1)
    ent2.insert(0, "0.1")

    Label(root, text="Xmax:").grid(row=1, column=2)
    ent3 = Entry(root, width=8)
    ent3.grid(row=1, column=3)
    ent3.insert(0, "10")

    Label(root, text="dx:").grid(row=1, column=4)
    ent4 = Entry(root, width=8)
    ent4.grid(row=1, column=5)
    ent4.insert(0, "0.05")

    Label(root, text="eps:").grid(row=1, column=6)
    ent5 = Entry(root, width=8)
    ent5.grid(row=1, column=7)
    ent5.insert(0, "0.0001")

    Button(root, text="Рисовать", command=Draw).grid(row=1, column=8)

    Label(root, text="b:").grid(row=2, column=0)
    ent6 = Entry(root, width=8)
    ent6.grid(row=2, column=1)
    ent6.insert(0, "1")

    Label(root, text="Шаг меток:").grid(row=2, column=2)
    ent7 = Entry(root, width=8)
    ent7.grid(row=2, column=3)
    ent7.insert(0, "1")

    Label(root, text="X:").grid(row=2, column=4)
    ent0 = Entry(root, width=8)
    ent0.grid(row=2, column=5)

    Label(root, text="Y:").grid(row=2, column=6)
    ent1 = Entry(root, width=8)
    ent1.grid(row=2, column=7)

    Button(root, text="Выход", command=window_deleted).grid(row=2, column=8)

    Draw()
    root.mainloop()