class Shape:
    """A base class to represent a geometric shape."""
    # counter = 0

    def __init__(self, shape_type, id = None):
        """Initialize the shape with a unique ID and type."""
        # if not id:
        #     Shape.counter += 1
        #     self.id = Shape.counter
        # else:
        self.id = id
        self.shape_type = shape_type

    def get_area(self):
        """Calculate and return the area of the shape."""
        pass

    def get_perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass

    def to_dict(self):
        """Return the shape properties as a dictionary."""
        pass