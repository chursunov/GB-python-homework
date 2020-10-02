"""
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randrange

try:
    with open("sum_numbers.txt", 'w+') as f_obj:
        for i in range(5):  # заполняем файл 5-ю случайными числами
            f_obj.write(str(randrange(1, 20)) + " ")
        f_obj.seek(0)  # переводим указатель в начало файла
        list_numbers = f_obj.read().split()
        summ_elements = 0
        for el in list_numbers:
            summ_elements += int(el)
        print(f"Сумма чисел в файле равна - {summ_elements}")
except IOError:
    print("Произошла ошибка ввода-вывода!")
