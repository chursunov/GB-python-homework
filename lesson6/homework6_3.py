"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position,
передать данные,
проверить значения атрибутов,
вызвать методы экземпляров).
"""


class Worker:
    name: str
    surname: str
    position: str
    _income: {}

    def __init__(self, name, surname, position) -> None:
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {}

    def add_income(self, wage: float = 0, bonus: float = 0):
        self._income['wage'] = wage
        self._income['bonus'] = bonus


class Position(Worker):

    def get_full_name(self):  # возвращает полное имя сотрудника
        return f"{self.name} {self.surname}"

    def get_total_income(self):  # возвращает доход с учетом премии
        return round(sum(self._income.values()), 2)


new_worker = Position("Aleksey", "Chursunov", "Business Analyst")
new_worker.add_income(250000, 500000)

print(new_worker.get_full_name())
print(new_worker.get_total_income())
