class Shape:
    counter = 0
    def __init__(self, shape_type):
        Shape.counter += 1
        self.id = Shape.counter
        self.shape_type = shape_type

    def get_area(self):
        pass

    def get_perimeter(self):
        pass

    def to_dict(self):
        pass