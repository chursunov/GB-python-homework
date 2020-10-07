"""
Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина),
width (ширина).

Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу:
длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
Проверить работу метода.

Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:

    def __init__(self, length, width) -> None:
        self._length = length
        self._width = width

    def calc_mass(self, mass_square_mq: float, thick_layer: float):
        return self._length * self._width * mass_square_mq * thick_layer / 1000


new_obj = Road(float(input("Введите длину полотна (в метрах) - ")),
               float(input("Введите ширину полотна (в метрах) - ")))
mass_square_meter = float(input('Введите массу 1 кв.м. асфальта, толщиной в 1 см. (в кг.) - '))
thickness_layer = float(input("Толщину полотна асфальта (в см) - "))
print(f"Потребуется асфальта, общей массой - {new_obj.calc_mass(mass_square_meter, thickness_layer)} тонн.")
