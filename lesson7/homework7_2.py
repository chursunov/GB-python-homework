"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).

Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.

Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    name: str

    @abstractmethod
    def material_consumptions(self):
        pass


class Suit(Clothes):

    def __init__(self, name, h: float) -> None:
        self.h = h
        self.name = name

    @property
    def material_consumptions(self):
        return 2 * self.h + 0.3


class Coat(Clothes):

    def __init__(self, name, v: float) -> None:
        self.v = v
        self.name = name

    @property
    def material_consumptions(self):
        return self.v / 6.5 + 0.5


class Consumptions(Clothes):
    result: float

    def __init__(self, clo: list, result=0):
        self.clo = clo
        self.result = result

    def material_consumptions(self):
        for item in self.clo:
            self.result = self.result + item.material_consumptions
        return round(self.result, 2)


suit = Suit("Armani", 60)
coat = Coat("Baker", 186)
cons = Consumptions([suit, coat])
print(f"Всего необходимо ткани - {cons.material_consumptions()}")
