import math
from src.Figure import Figure


# класс круг наследник класса Фигура
class Circle(Figure):
    def __init__(self, side1):
        self.side1 = side1
        if not isinstance(self.side1, (int, float)):
            raise ValueError('Значение не является числом')
        elif self.side1 < 0:
            raise ValueError('Значение не может быть отрицательным')
        self.name = 'circle'

    # метод расчета площади фигуры
    @property
    def area(self):
        return math.pi * (self.side1 ** 2)

    # метод расчета периметра фигуры
    @property
    def perimeter(self):
        return 2 * math.pi * self.side1
