from math import sqrt
from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, name, a, b, c):
        super().__init__(name, a, b, c, a)
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


triangle = Triangle('tri1', 13, 14, 15)
print(triangle.area())
print(triangle.perimeter())
