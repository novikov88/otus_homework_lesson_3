class Figure:
    def add_area(self, name):
        if isinstance(name, Figure):
            return self.area + name.area
        else:
            raise ValueError("ValueError Incorrect class")
