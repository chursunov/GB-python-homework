"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3,
а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.
"""
from itertools import count, cycle
import random


def count_func(numbers, count_numbers):
    i = 0
    for el in count(numbers):
        if i == count_numbers:
            break
        print(el, end=" ")
        i += 1


def cycle_func(list_numbers, count_iteration):
    i = 0
    for el in cycle(list_numbers):
        if i == count_iteration:
            break
        print(el, end=" ")
        i += 1


start_number = int(input("Введите начальное число: "))
count_numbers = int(input("Введите количество генерируемых чисел: "))
count_func(start_number, count_numbers)

list_numbers = [random.randrange(0, 100) for el in range(0, 20)]
print("\n Список для повторения (из 20 элементов): ", list_numbers)
count_iteration = int(input("Ведите количество повторяемых элементов (от 1 до 20)- "))
cycle_func(list_numbers, count_iteration)
