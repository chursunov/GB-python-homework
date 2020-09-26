"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
import sys

try:
    file, hour_job, tariff, bonus = sys.argv
except ValueError:
    print("Вы должны указать 3 параметра (выработка в часах, ставка, премия)!")
    exit()


def salary(hour_job, tariff, bonus):
    return hour_job * tariff + bonus


print(f"Выработка в часах - {hour_job} ч.\nСтавка в час - {tariff} р.\nПремия - {bonus} р.")
result_salary = salary(int(hour_job), int(tariff), int(bonus))
print(f"Зарплата сотрудника - {result_salary} р.")
