try:
    month = int(input("Введите месяц в виде целого числа от 1 до 12 --> "))
except ValueError:
    print("Вы ввели не число!")
    exit()

if month < 1 or month > 12:
    print("Такого месяца не существует")
    exit()

seasons = {
    12: "зима", 1: "зима", 2: "зима",
    3: "весна", 4: "весна", 5: "весна",
    6: "лето", 7: "лето", 8: "лето",
    9: "осень", 10: "осень", 11: "осень"
}
print(f"Ваш месяц относится к времени года - {seasons.get(month)}")

