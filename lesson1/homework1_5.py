proceeds = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))

if proceeds > costs:
    profit = proceeds - costs
    print("Фирма прибыльна, прибыль составляет: ", profit)
    profitability = (profit / proceeds) * 100
    print("Рентабельность составляет: %02d %% " % profitability)
    number_employees = int(input("Введите количество сотрудников фирмы: "))
    print("Прибыль фирмы в расчете на одного сотрудника составляет: ", profit / number_employees)
elif proceeds < costs:
    print("Фирма убыточна, убыток составляет: ", proceeds - costs)
else:
    print("Фирма работает в 0")
