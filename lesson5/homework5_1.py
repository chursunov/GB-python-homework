"""
Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

try:
    with open("text.txt", 'w+') as f_obj:
        print("Введите несколько строк данных. Для завершения нажмите 2 раза Enter: \n ")
        while True:
            user_string = input()
            if user_string == "":
                break
            print(user_string, file=f_obj)

except IOError:
    print("Произошла ошибка ввода-вывода!")
