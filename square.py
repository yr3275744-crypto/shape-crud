from shape import Shape
import logger_setup

class Square(Shape):
    """docstring"""
    def __init__(self, shape_type, side):
        """docstring"""
        super().__init__(shape_type)
        self.logger = logger_setup.create_manage_shape_logger()
        self.side = float(side)
        self.logger.info("the square created successfully")
    
    def get_area(self):
        """docstring"""
        return self.side ** 2

    def get_perimeter(self):
        """docstring"""
        return self.side * 4

    def to_dict(self):
        """docstring"""
        the_shape = {"id":self.id, "type":self.shape_type, "side":self.side}
        return the_shape
    
if __name__ == "__main__":
    try:
        a_squer = Square("square", 5)
        print(a_squer.get_area())
        print(a_squer.get_perimeter())
        print(a_squer.to_dict())
    except Exception as e:
        logger = logger_setup.creat_manage_shape_logger()
        logger.exception(e)