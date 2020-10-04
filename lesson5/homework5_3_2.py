"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
numerals = {
    '1': "Один",
    '2': "Два",
    '3': "Три",
    '4': "Четыре"
}

try:
    with open("numbers.txt") as f_obj, open("new_numbers.txt", "x") as new_f_obj:
        for content in f_obj:
            temp = content.split()
            print(f"{numerals.get(temp[2])} - {temp[2]}", file=new_f_obj)

except IOError:
    print("Произошла ошибка ввода-вывода!")