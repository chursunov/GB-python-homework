a = float(input("Введите a >>"))
b = float(input("Введите b >>"))
result = a
day = 1

while True:
    if b <= result:
        print(f"{day}-й день: {result} км")
        print(f"На {day}-й день спортсмен достиг результата — не менее {b} км")
        break
    else:
        print(f"{day}-й день: {result} км")
        result = round(result + result * 0.1, 2)
    day += 1



