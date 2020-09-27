"""
Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.

Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
from random import shuffle

list_numbers = [el for el in range(0, 20)]
shuffle(list_numbers)
print(list_numbers)
result_list = []
for i in range(len(list_numbers) - 1):
    if list_numbers[i + 1] > list_numbers[i]:
        result_list.append(list_numbers[i + 1])
print(result_list)
