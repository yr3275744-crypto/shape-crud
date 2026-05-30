from shape import Shape
import logger_setup

class Rectangle(Shape):
    """docstring"""
    def __init__(self, shape_type, length_side, width_side):
        """docstring"""
        super().__init__(shape_type)
        self.logger = logger_setup.create_manage_shape_logger()
        self.length_side = float(length_side)
        self.width_side = float(width_side)
        self.logger.info("the rectangle created successfully")
    
    def get_area(self):
        """docstring"""
        return self.langth_side * self.width_side
        

    def get_perimeter(self):
        """docstring"""
        return 2 * self.length_side + 2 * self.width_side

    def to_dict(self):
        """docstring"""
        the_shape = {"id":self.id, "type":self.shape_type, "length side":self.length_side, "width side":self.width_side}
        return the_shape
    
if __name__ == "__main__":
    try:
        a_squer = Rectangle("rectangle", 5, 4)
        print(a_squer.get_area)
        print(a_squer.get_perimeter())
        print(a_squer.to_dict())
    except Exception as e:
        logger = logger_setup.creat_manage_shape_logger()
        logger.exception(e)