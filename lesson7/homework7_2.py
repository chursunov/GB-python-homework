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

    # def __init__(self, name) -> None:
    #     self.name = name

    @abstractmethod
    def material_consumptions(self):
        pass


class Suit(Clothes):

    def __init__(self, name, h: float) -> None:
        self.h = h
        self.name = name
        # super().__init__(name)

    def material_consumptions(self):
        return 2 * self.h + 0.3


class Coat(Clothes):

    def __init__(self, name, v: float) -> None:
        self.v = v
        self.name = name
        # super().__init__(name)

    def material_consumptions(self):
        return self.v / 6.5 + 0.5


class Consumptions(Clothes):
    result: float

    def __init__(self, clo: list):
        self.clo = clo

    def material_consumptions(self):
        self.result = 0
        for item in self.clo:
            self.result = self.result + float(item.material_consumptins())
        return self.result


suit = Suit("Armani", 50)
coat = Coat("Baker", 186)
cons = Consumptions([suit, coat])
print(cons.material_consumptions())
print(round(suit.material_consumptions(), 2))
print(round(coat.material_consumptions(), 2))
