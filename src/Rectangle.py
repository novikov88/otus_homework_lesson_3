from src.Figure import Figure


# класс прямоугольник наследник класса Фигура
class Rectangle(Figure):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        if not isinstance(self.side1, (int, float)) or not isinstance(self.side2, (int, float)):
            raise ValueError('Значение не является числом')
        elif self.side1 < 0 or self.side2 < 0:
            raise ValueError('Значение не может быть отрицательным')
        self.name = 'rectangle'

    # метод расчета площади фигуры
    @property
    def area(self):
        return self.side1 * self.side2

    # метод расчета периметра фигуры
    @property
    def perimeter(self):
        return (self.side1 + self.side2) * 2
