"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, color: str, name: str, speed: int, is_police: bool = False) -> None:
        self.color = color
        self.name = name
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction: str):
        if direction == "left":
            print("Машина повернула налево")
        elif direction == "right":
            print("Машина повернула направо")
        else:
            print("Повторите ввод поворота (left или right)!")

    def show_speed(self):
        print(f"Текущая скорость автомобиля - {self.speed} км/ч")


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f"Текущая скорость - {self.speed} км/ч Первышение скорости в 60 км/ч !! ")
        else:
            print(f"Текущая скорость автомобиля - {self.speed} км/ч")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Первышение скорости 40 км/ч !! Текущая скорость - {self.speed} км/ч")
        else:
            print(f"Текущая скорость автомобиля - {self.speed} км/ч")


class PoliceCar(Car):
    pass


def info(class_object, direction: str):
    print(f"Название: {class_object.name}, Цвет: {class_object.color}, Скорость: {class_object.speed}")
    class_object.go()
    class_object.turn(direction)
    class_object.show_speed()
    class_object.stop()
    if class_object.is_police:
        print("Это полицейская машина!")


ford = TownCar("black", "Ford", 100)
ferrari = SportCar("red", "Ferrari", 200)
bus = WorkCar("yellow", "Bus", 50)
police = PoliceCar("blue", "Mustang", 120, True)

info(ford, "left")
info(ferrari, "right")
info(bus, "right")
info(police, "left")
