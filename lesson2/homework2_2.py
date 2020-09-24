# вводим количество элементов в списке и проверяем на ввод числа
try:
    length_list = int(input("Введите количество элементов в списке - "))
except ValueError:
    print("Вы ввели не число!")
    exit()

# создаем и заполняем список
my_list = []
for i in range(length_list):
    my_list.append(input(f"Введите {i + 1}-й элемент списка ->> "))

k = 0
for i in range(len(my_list) // 2):
    my_list[k], my_list[k + 1] = my_list[k + 1], my_list[k]  # обмениваем местами элементы [к] и [к+1] через кортежи
    k += 2

print(my_list)
