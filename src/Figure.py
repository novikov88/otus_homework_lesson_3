class Figure:
    def __init__(self, name, a, b, c, d):
        self.name = name
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def area(self):
        return self.a ** 2
