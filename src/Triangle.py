from math import sqrt
from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
            raise ValueError('Треугольник не может быть создан по заданным параметрам')
        elif not isinstance(self.side1, (int, float)) \
                or not isinstance(self.side2, (int, float) or not isinstance(self.side3, (int, float))):
            raise ValueError('Значение не является числом')
        self.name = 'triangle'

    @property
    def area(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        return sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))

    @property
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
