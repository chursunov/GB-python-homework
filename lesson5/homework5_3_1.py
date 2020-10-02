"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет
оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

try:
    with open("workers.txt") as f_obj:
        content = f_obj.readlines()
        average_salary = 0
        for f_str in content:
            temp = f_str.split()
            if float(temp[1]) < 20000:
                print(temp[0])
            average_salary += float(temp[1])
        print("Средняя зарплата сотрудников: ", average_salary / len(content))
except IOError:
    print("Произошла ошибка ввода-вывода!")
