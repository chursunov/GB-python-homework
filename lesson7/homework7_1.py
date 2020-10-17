"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: см. в методичке.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:

    def __init__(self, matrix_list: list) -> None:
        self.matrix_list = matrix_list

    def __str__(self):
        for el in self.matrix_list:
            print(" ".join(map(str, el)))
        return ""

    def __add__(self, other):
        result = []
        for i in range(len(self.matrix_list)):
            temp_list = list(map(lambda x, y: x + y, self.matrix_list[i], other.matrix_list[i]))
            result.append(temp_list)
        return result


matrix = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]])
matrix_1 = Matrix([[2, 2, 2], [1, 1, 1], [4, 4, 4], [0, 0, 0]])
print(matrix)
print(matrix_1)
result_matrix = Matrix(matrix + matrix_1)
print(result_matrix)
