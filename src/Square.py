from src.Figure import Figure


# класс квадрат наследник класса Фигура
class Square(Figure):
    def __init__(self, side):
        self.side = side
        if not isinstance(self.side, (int, float)):
            raise ValueError('Значение не является числом')
        elif self.side < 0:
            raise ValueError('Значение не может быть отрицательным')
        self.name = 'square'

    # метод расчета площади фигуры
    @property
    def area(self):
        return self.side ** 2

    # метод расчета периметра фигуры
    @property
    def perimeter(self):
        return 4 * self.side
