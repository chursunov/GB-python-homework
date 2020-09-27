"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""
import random

list_numbers = [random.randrange(0, 100) for el in range(0, 20)]
print("Исходный список - ", list_numbers)
new_list_numbers = []
for element in list_numbers:
    if list_numbers.count(element) == 1:
        new_list_numbers.append(element)
print("Результат", new_list_numbers)
