from src.Figure import Figure


class Square(Figure):
    def __init__(self, name, a):
        super().__init__(name, a, a, a, a)
        self.a = a

    def perimeter(self):
        return 4 * self.a


square = Square('sq1', 3)
print(square.area())
print(square.perimeter())
