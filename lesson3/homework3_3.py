"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов."""


def my_func(a, b, c):
    if a <= b and a < c:
        return b + c
    elif b <= a and b < c:
        return a + c
    else:
        return a + b


print(my_func(1, 2, 3))
