number = input("Введите любое число n >> ")
summ_number = int(number)
str_number = number

for i in range(2):
    str_number = str_number + number
    summ_number += int(str_number)

print("Сумма чисел n+nn+nnn равна >> ", summ_number)
