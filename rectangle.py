from shape import Shape

class Rectangle(Shape):
    """docstring"""
    def __init__(self,shape_id, length_side, width_side):
        """docstring"""
        super().__init__(shape_id,"rectangle")
        self.length_side = length_side
        self.width_side = width_side
    
    def get_area(self):
        """docstring"""
        return self.langth_side * self.width_side
        

    def get_perimeter(self):
        """docstring"""
        return 2 * self.langth_side + 2 * self.width_side

    def to_dict(self):
        """docstring"""
        the_shape = {"id":self.id, "type":self.shape_type, "length side":self.length_side, "width side":self.width_side}
        return the_shape
    
if __name__ == "__main__":
    a_squer = Rectangle(123, 5, 4)
    print(a_squer.to_dict())