"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class MyDate:
    def __init__(self, date: str) -> None:
        self.date = date

    @classmethod
    def date_to_int(cls, date: str):
        date_list = map(int, date.split("-"))
        day, month, year = date_list
        return day, month, year

    @staticmethod
    def validate(day, month, year):
        if day in set(range(1, 31)):
            print("День прошел валидацию")
        else:
            print("Такого дня не существует!")
        if month in set(range(1, 12)):
            print("Месяц прошел валидацию")
        else:
            print("Такого месяца не существует!")
        if year:
            print("Год прошел валидацию")
        else:
            print("Такого года не существует!")


user_date = input("Введите дату: ")
day, month, year = MyDate.date_to_int(user_date)
MyDate.validate(day, month, year)
