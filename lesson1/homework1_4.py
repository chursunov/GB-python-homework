str_number = input("Введите любое целое положительное число >> ")
max_number = 0

for number in str_number:
    if int(number) > max_number:
        max_number = int(number)

print("Cамая большая цифра в числе >> ", max_number)
