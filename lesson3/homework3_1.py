def division(a, b):
    try:
        print("Результат: a / b = ", a / b)
    except ZeroDivisionError:
        print("Вы пытаетесь поделить на ноль!")


a = float(input("Введите число а:"))
b = float(input("Введите число b:"))
division(a, b)
