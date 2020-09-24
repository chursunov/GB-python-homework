try:
    month = int(input("Введите месяц в виде целого числа от 1 до 12 --> "))
except ValueError:
    print("Вы ввели не число!")
    exit()

if month < 1 or month > 12:
    print("Такого месяца не существует")
    exit()

seasons = ["зима", "весна", "лето", "осень"]

if 12 == month or 1 <= month <= 2:
    print(f"Ваш месяц относится к времени года - {seasons[0]}")
elif 3 <= month <= 5:
    print(f"Ваш месяц относится к времени года - {seasons[1]}")
elif 6 <= month <= 8:
    print(f"Ваш месяц относится к времени года - {seasons[2]}")
else:
    print(f"Ваш месяц относится к времени года - {seasons[3]}")
