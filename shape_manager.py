import json
import logger_setup
from shape import Shape
from square import Square
from rectangle import Rectangle
from circle import Circle

class ShapeManager:
    """A class to manage, store, and modify geometric shapes."""

    def __init__(self, json_file_path: str) -> None:
        """Initialize the manager and load existing shapes from a JSON file."""
        self.logger = logger_setup.create_manage_shape_logger()
        self.shapes = []
        self.json_file = json_file_path
        self.shape_classes = {"square": Square, "rectangle": Rectangle, "circle": Circle}
        self.create_dict_functions = {"circle": self.create_circle_dict, 
                                      "square": self.create_square_dict, 
                                      "rectangle": self.create_rectangle_dict}
        self.load_from_json()
    
    def create_circle_dict(self) -> dict:
        """Prompt the user for circle dimensions and return them as a dictionary."""
        radius = float(input("Enter the radius: "))
        if radius < 0:
            raise ValueError("You must enter a positive number.")
        return {"type": "circle", "radius": radius}

    def create_square_dict(self) -> dict:
        """Prompt the user for square dimensions and return them as a dictionary."""
        side = float(input("Enter the side value: "))
        if side < 0:
            raise ValueError("You must enter a positive number.")
        return {"type": "square", "side": side}

    def create_rectangle_dict(self) -> dict:
        """Prompt the user for rectangle dimensions and return them as a dictionary."""
        length_side = float(input("Enter the length side value: "))
        width_side = float(input("Enter the width side value: "))
        if length_side < 0 or width_side < 0:
            raise ValueError("You must enter a positive number.")
        return {"type": "rectangle", "length_side": length_side, "width_side": width_side}

    def create_shape(self, shape_dict: dict) -> object | None:
        """Instantiate and return a specific Shape object from a dictionary."""
        mapping = {"type": "shape_type", "length side": "length_side", "width side": "width_side"}
        translated_dict = {}
        id = None
        for k, v in shape_dict.items():
            if k in mapping:
                translated_dict[mapping[k]] = v
            else:
                translated_dict[k] = v
        if translated_dict.get("id"):
            id = translated_dict.pop("id")
        return self.shape_classes[translated_dict["shape_type"]](**translated_dict, id = id)
        
    def add_shape(self, shape: object) -> None:
        """Add a shape object to the internal shapes list."""
        self.shapes.append(shape)
        return None

    def get_all_shapes(self) -> list:
        """Return a list of all shapes converted to dictionaries."""
        shapes_list = []
        for shape in self.shapes:
            shapes_list.append(shape.to_dict())
        return shapes_list
    
    def show_all_shapes(self):
        """Print all shapes."""
        shapes_list = self.get_all_shapes()
        if not shapes_list:
            print("There are no shapes to display yet.")
        for shape_dict in shapes_list:
            print(shape_dict)
        return None

    def update_shape(self, shape_id: int) -> bool:
        """Find and update a shape's data by its ID."""
        is_updated = False
        for shape in self.shapes:
            if shape.id == shape_id:
                shape_dict = shape.to_dict()
                shape_type = shape_dict["type"]
                new_data = self.create_dict_functions[shape_type]()
                shape_dict.update(**new_data)
                self.shapes.remove(shape)
                shape = self.create_shape(shape_dict)
                self.add_shape(shape) 
                is_updated = True 
                break
        return is_updated
    
    def delete_shape(self, shape_id: int) -> bool:
        """Remove a shape from the list by its ID."""
        is_deleted = False
        for shape in self.shapes:
            if shape.id == shape_id:
                self.shapes.remove(shape)
                is_deleted = True
                break
        return is_deleted

    def add_shape_handle(self) -> None:
        """Handle user input to create, add, and save a new shape."""
        try:
            shape_name = input("Enter the shape you want add: ")
            shape_dict = self.create_dict_functions[shape_name]()
        except KeyError as e:
            self.logger.exception(e)
            raise KeyError("The shape does not exists.")
        except ValueError as e:
            self.logger.exception(e)
            raise ValueError("The value is invalid.")

        shape_object = self.create_shape(shape_dict)
        self.add_shape(shape_object)
        self.save_to_json()
        self.logger.info("the shape was added succeffully.")
        print("the shape was added succeffully.")
        return None

    def update_shape_handle(self) -> bool:
        """Handle user input to find and update a shape by ID."""
        try:
            shape_id = int(input("Enter the shape id: "))
            is_updated = self.update_shape(shape_id)
            if is_updated:
                self.save_to_json()
                self.logger.info("The shape updated successfully.")
                print("The shape updated successfully.")
        except ValueError as e:
            self.logger.exception(e)
            raise ValueError("The value is invalid.")
        
    def remove_shape_handle(self) -> bool:
        """Handle user input to delete a shape by ID."""
        try:
            shape_id = int(input("Enter the shape id: "))
            is_deleted = self.delete_shape(shape_id)
            self.save_to_json()
            if is_deleted:
                self.logger.info(f"The shape {shape_id} is deleted succesffully.")
        except ValueError as e:
            self.logger.exception(e)
            raise ValueError("The value is invalid.")

    def save_to_json(self):
        """Save the current shapes list to the JSON file."""
        is_saved = False
        shapes_list = self.get_all_shapes()
        with open(self.json_file, "w") as f:
            json.dump(shapes_list, f)
        is_saved = True
        self.logger.info("The json file is updated.")
        return is_saved
 
    def load_from_json(self) -> None:
        """Load shapes from the JSON file and populate the internal list."""
        try:
            with open(self.json_file, "r") as f:
                list_shapes_dicts = json.load(f)
            for shape in list_shapes_dicts:
                self.add_shape(self.create_shape(shape))
        except FileNotFoundError as e:
            self.logger.exception(e)
            self.save_to_json()
        except json.decoder.JSONDecodeError as e:
            self.logger.exception(e)
            raise ValueError("The file is empty.")
        except KeyError as e:
            self.logger.exception(e)
            raise KeyError("The shape does not exists.")
        return None