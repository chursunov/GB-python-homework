"""
1. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""
"""
2. Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
"""
"""
3. Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


class Peripherals:
    name: str  # название
    manufacturer: str  # производитель
    paper_size: str  # размер бумаги
    wi_fi: bool  # наличие Wi-fi
    automatic_feeder: bool  # наличие автоматической подачи листов

    def __init__(self, name, manufacturer, paper_size, wi_fi, automatic_feeder) -> None:
        self.name = name
        self.manufacturer = manufacturer
        self.wi_fi = wi_fi
        self.paper_size = paper_size
        self.automatic_feeder = automatic_feeder


class Printer(Peripherals):
    print_speed: int  # скорость печати
    is_colour: bool  # печать цветная или нет
    duplex_printing: bool  # двусторонняя печать

    def __init__(self, name, manufacturer, paper_size, wi_fi, automatic_feeder, print_speed, is_colour,
                 duplex_printing) -> None:
        super().__init__(name, manufacturer, paper_size, wi_fi, automatic_feeder)
        self.print_speed = print_speed
        self.is_colour = is_colour
        self.duplex_printing = duplex_printing


class Scanner(Peripherals):
    scanning_speed: int  # скорость сканирования
    scanner_resolution: str  # разрешение
    is_flatbed_scanner: bool  # это планшетный сканер
    is_handheld_scanner: bool  # это портативный сканер

    def __init__(self, name, manufacturer, paper_size, wi_fi, automatic_feeder, scanning_speed, scanner_resolution,
                 is_flatbed_scanner=False, is_handheld_scanner=False) -> None:
        super().__init__(name, manufacturer, paper_size, wi_fi, automatic_feeder)
        self.scanning_speed = scanning_speed
        self.scanner_resolution = scanner_resolution
        self.is_flatbed_scanner = is_flatbed_scanner
        self.is_handheld_scanner = is_handheld_scanner


class Copy(Peripherals):
    copy_speed: int  # скорость копирования
    is_colour: bool  # цветной
    max_number_copy_per_cycle: int  # рекомендуемый объем копирования в мес

    def __init__(self, name, manufacturer, paper_size, wi_fi, automatic_feeder, copy_speed, is_colour,
                 max_number_copy_per_cycle) -> None:
        super().__init__(name, manufacturer, paper_size, wi_fi, automatic_feeder)
        self.copy_speed = copy_speed
        self.is_colour = is_colour
        self.max_number_copy_per_cycle = max_number_copy_per_cycle


# склад компании
class Storage:
    capacity: int  # вместимость склада, шт.
    peripherals: list  # список техники в компании

    def __init__(self, capacity=50) -> None:
        self.capacity = capacity
        Storage.peripherals = []

    def acceptance_to_storage(self, item: object):
        self.peripherals.append(item)


# компания
class Company:
    peripherals_list: list

    def __init__(self, count=0) -> None:
        self.count = count
        self.peripherals_list = []

    def receives_equipment(self, item: object):
        self.peripherals_list.append(item)


storage = Storage()
company = Company()
printer = Printer("ML-1210", "Samsung", "A4", False, True, 26, False, True)
scanner = Scanner("X1", "Canon", "A4", False, False, 15, 2400, True)
copy_man = Copy("C1", "Xerox", "A4", False, False, 18, True, 500)

storage.acceptance_to_storage(printer)
storage.acceptance_to_storage(scanner)
storage.acceptance_to_storage(copy_man)
print(f"На складе - {len(storage.peripherals)} ед. оборудования")
company.receives_equipment(storage.peripherals.pop(1))
print(f"На складе осталось - {len(storage.peripherals)} ед. оборудования")
print(f"В компании теперь - {len(company.peripherals_list)} ед. оборудования")
