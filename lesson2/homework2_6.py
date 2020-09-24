# создаем элемент списка кортежей
number_element = 1
product_list = []
while True:
    temp_list = []
    product_name = input("Введите название товара: ")
    product_price = int(input("Введите цену товара: "))
    product_quantity = int(input("Введите количество товара: "))
    product_unit = input("Введите единицу измерения товара: ")
    temp_dict = dict(название=product_name, цена=product_price, количество=product_quantity, ед=product_unit)
    temp_list.append(number_element)
    temp_list.append(temp_dict)
    temp_tuple = tuple(temp_list)
    product_list.append(temp_tuple)
    number_element += 1
    exit_sign = input("Если вы хотите закончить вводить данные, нажмите пробел")
    if exit_sign == " ":
        break
# тестовый набор данных, можно раскомментить и не придется вводить вручную все данные
# product_list = [
#     (1, {'название': 'блокнот', 'цена': 54, 'количество': 5, 'ед': 'шт.'}),
#     (2, {'название': 'скрепка', 'цена': 158, 'количество': 6, 'ед': 'шт.'}),
#     (3, {'название': 'ранец', 'цена': 666, 'количество': 9, 'ед': 'шт.'}),
#     (4, {'название': 'ремонт', 'цена': 1000, 'количество': 1, 'ед': 'усл.'})
# ]

# получаем список всех ключей
tmp_list = list(product_list[0])
key_list = tmp_list[1].keys()
# создаем словарь с ключами и значениями
result_dict = {}
for el in key_list:
    result_dict.setdefault(el, [])
# перебираем структуру данных Товары и заполняем итоговый словарь значениями
for key in key_list:
    tmp_list1 = []
    for element_list in product_list:
        tmp_list1.append(element_list[1].get(key))  # создаем список со всеми значениями по каждому ключу
    result_dict.update({key: tmp_list1})

print(result_dict)
