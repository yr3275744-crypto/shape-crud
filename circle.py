from shape import Shape
from math import pi
import logger_setup

class Circle(Shape):
    """A class to represent a circle shape."""
    
    def __init__(self, shape_type, radius, id = None):
        """Initialize the circle with a shape type and radius."""
        super().__init__(shape_type, id)
        self.logger = logger_setup.create_manage_shape_logger()
        self.radius = float(radius)
        self.logger.info("the circle created successfully")
    
    def get_area(self):
        """Calculate and return the area of the circle."""
        return (self.radius ** 2) * pi
    
    def get_perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle."""
        return 2 * self.radius * pi
    
    def to_dict(self):
        """Return the circle properties as a dictionary."""
        the_shape = {"id":self.id, "type":self.shape_type, "radius":self.radius}
        return the_shape
    
if __name__ == "__main__":
    try:
        a_circ = Circle("circle", 20)
        print(a_circ.get_area())
        print(a_circ.get_perimeter())
        print(a_circ.to_dict())
    except Exception as e:
        logger = logger_setup.creat_manage_shape_logger()
        logger.exception(e)