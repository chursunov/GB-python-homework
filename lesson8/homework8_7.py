"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""
import re


class ComplexNumber:
    number: list

    def __init__(self, number_x) -> None:
        self.number = re.findall(r'\d', number_x)

    def __add__(self, other):
        temp = int(self.number[0]) + int(other.number[0])
        temp2 = int(self.number[1]) + int(other.number[1])
        return f"{temp} + {temp2}х"

    def __mul__(self, other):
        temp = int(self.number[0]) * int(other.number[0])
        temp2 = int(self.number[1]) * int(other.number[1])
        return f"{temp} + {temp2}х"


a = ComplexNumber("1+3x")
b = ComplexNumber("3+2x")

print(a + b)
print(a * b)
