"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivByZeroException(Exception):
    def __str__(self):
        return "Ошибка деления на ноль!"


def division(a, b):
    if b == 0:
        raise DivByZeroException
    else:
        return a / b


a = int(input("Введите делимое - "))
b = int(input("Введите делитель - "))
try:
    print(division(a, b))
except DivByZeroException as exception:
    print("Вы пытаетесь поделить на ноль!!")
