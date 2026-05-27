from shape import Shape
from logger_setup import manage_shapes_logger as logger
from math import pi

class Circle(Shape):
    """docstring"""
    def __init__(self, shape_type, radius):
        """docstring"""
        super().__init__(shape_type)
        self.radius = float(radius)
        logger.info("the circle created successfully")
    
    def get_area(self):
        """docstring"""
        return (self.radius ** 2) * pi
    
    def get_perimeter(self):
        """docstring"""
        return 2 * self.radius * pi
    
    def to_dict(self):
        """docstring"""
        the_shape = {"id":self.id, "type":self.shape_type, "radius":self.radius}
        return the_shape
    
if __name__ == "__main__":
    try:
        a_circ = Circle("circle", 20)
        print(a_circ.get_area())
        print(a_circ.get_perimeter())
        print(a_circ.to_dict())
    except Exception as e:
        logger.exception(e)