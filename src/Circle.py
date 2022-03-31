import math
from src.Figure import Figure


class Circle(Figure):
    def __init__(self, name, a):
        super().__init__(name, a, a, a, a)
        self.a = a

    def area(self):
        return math.pi * (self.a ** 2)

    def perimeter(self):
        return 2 * math.pi * self.a


circle = Circle('cir1', 10)
print(circle.area())
print(circle.perimeter())
