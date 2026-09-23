try:
    x = float(input("Введите x: "))
    y = float(input("Введите y: "))
    r = float(input("Введите r: "))

    if r<0:
        print("Радиус не может быть отрицательным.")
    elif (x<=0 and y<=0 and y>=-x-r) or(x>=0 and y>=0 and y**2<=r**2 - x**2):
        print("Попадает в область")
    else:
        print("Не попадает в область")
except ValueError:
    print("Не возможно преобразовать входные данные.")