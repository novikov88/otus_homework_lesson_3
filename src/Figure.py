"""
Вторая домашняя работа
Дата: 04.04.22
Задание: создать базовый класс и дочерние классы. Реализовать методы получения площади и периметра, также
разработать метод сумм площадей двух фигур через add_area. Покрыть тестами код.
"""


class Figure:
    # метод получения сумм площадей фигур если передана фигура базового класса, иначе ошибка
    def add_area(self, name):
        if isinstance(name, Figure):
            return self.area + name.area
        else:
            raise ValueError("ValueError Incorrect class")

    # метод удаления экземпляра класса
    def __del__(self):
        pass
