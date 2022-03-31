from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, name, a, b):
        super().__init__(name, a, b, a, b)
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return (self.a + self.b) * 2


rectangle = Rectangle('rec1', 2, 3)
print(rectangle.area())
print(rectangle.perimeter())
