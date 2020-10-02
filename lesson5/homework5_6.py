"""
Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json

result_list = []
dict_firms = {}
interim_list = []
try:
    with open("firms.txt") as f_obj:
        average_profit = 0
        count = 0
        for f_str in f_obj:
            temp_firm = f_str.split()
            profit = int(temp_firm[2]) - int(temp_firm[3])
            if profit > 0:
                average_profit += profit
                count += 1
            firms_profit_tuple = tuple([temp_firm[0], profit])
            interim_list.append(firms_profit_tuple)
        dict_firms = dict(interim_list)
        result_list.append(dict_firms)
        result_list.append(dict(average_profit=average_profit / count))
        print(result_list)
    with open('firms.json', 'w') as file_json:
        json.dump(result_list, file_json)
except IOError:
    print("Произошла ошибка ввода-вывода!")
