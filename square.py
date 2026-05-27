from shape import Shape

class Square(Shape):
    """docstring"""
    def __init__(self,shape_id, side):
        """docstring"""
        super().__init__(shape_id,"square")
        self.side = side
    
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
    a_squer = Square(123, 5)
    print(a_squer.get_area())
    print(a_squer.get_perimeter())
    print(a_squer.to_dict())