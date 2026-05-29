import json
import logger_setup
from shape import Shape
from square import Square
from rectangle import Rectangle
from circle import Circle
SHAPE_CLASSES = {"square":Square, "rectangle":Rectangle, "circle":Circle}

class ShapeManager:
    """docstring"""
    def __init__(self, json_file_path:str) -> None:
        """docstring"""
        self.logger = logger_setup.creat_manage_shape_logger()
        self.shapes = []
        self.load_from_json(json_file_path)
        self.creat_dict_functions = {"circle":self.create_circle_dict, 
                                   "square":self.create_square_dict, 
                                   "rectangle":self.create_rectangle_dict}
    
    def create_circle_dict(self) -> dict:
        """docstring"""
        radius = float(input("Enter the radius: "))
        return {"type": "circle", "radius":radius}


    def create_square_dict(self) -> dict:
        """docstring"""
        side = float(input("Enter the side value: "))
        return {"type": "square", "side":side}
        

    def create_rectangle_dict(self) -> dict:
        """docstring"""
        length_side = float(input("Enter the length side value: "))
        width_side =  float(input("Enter the width side value: "))
        return {"type": "square", "length_side":length_side, "width_side":width_side}

    def create_shape(self, shape:dict) -> object | None:
        """docstring"""
        return SHAPE_CLASSES[shape["type"]](**shape)
        
    def add_shape(self, shape:object) -> None:
        """docstring"""
        self.shapes.append(shape)
        return None

    def get_all_shapes(self) -> list:
        """docstring"""
        shapes_list = []
        
        for shape in self.shapes:
            shapes_list.append(shape.to_dict())
        
        return shapes_list
    
    def update_shape(self, shape_id:int, new_data:dict) -> bool:
        """docstring"""
        is_updated = False
        for shape in self.shapes:
            if shape.id == shape_id:
                shape_dict = shape.to_dict()
                shape_dict.update(shape_id, **new_data)
                self.shapes.remove(shape)
                Shape.counter -= 1
                self.add_shape(self.create_shape(shape_dict)) 
                is_updated = True 
        
        return is_updated
    
    def delete_shape(self, shape_id:int) -> bool:
        """docstring"""
        is_deleted = False
        
        for shape in self.shapes:
            if shape.id == shape_id:
                self.shapes.remove(shape)
                is_deleted = True
        
        return is_deleted

    def add_shape_handle(self, file_path:str) -> None:
        """docstring"""
        try:
            shape_name = input("Enter the shape you want add: ")
            shape_dict = self.create_dict_functions(shape_name)
        
        except KeyError:
            raise KeyError("The shape does not exists.")
        
        except ValueError:
            raise ValueError("The value is invalid.")

        shape_object = self.create_shape(shape_dict)
        self.add_shape(shape_object)
        self.save_to_json(file_path)
        
        return None


    def update_shape_handle(self, file_path:str, create_dict_functions:dict) -> bool:
        """docstring"""
        try:
            shape_id = int(input("Enter the shape id: "))
            new_data = self.add_shape_handle(self, file_path, create_dict_functions)
            is_updated = self.update_shape(shape_id, new_data)
            return is_updated
        
        except ValueError as e:
            raise e("The value is invalid.")
        
    def remove_shape_handle(shape_manager:ShapeManager, file_path:str, create_dict_functions:dict) -> None:
        """docstring"""
        try:
            shape_id = int(input("Enter the shape id: "))
            return ShapeManager.delete_shape(shape_id)
        except ValueError as e:
            raise e("The value is invalid.")

    def save_to_json(self, json_file_path:str):
        """docstring"""
        is_saved = False
        shapes_list = self.get_all_shapes()
        
        with open(json_file_path, "w") as f:
            json.dump(shapes_list, f)
        
        is_saved = True

        return is_saved
 
    def load_from_json(self, json_file_path:str) -> None:
        """docstring"""
        try:
            with open(json_file_path, "r") as f:
                list_shapes_dicts = json.load(f)
            
            for shape in list_shapes_dicts:
                self.add_shape(self.create_shape(shape))
        
        except json.decoder.JSONDecodeError as e:
            self.logger.exception(e)
            raise e("the json file is empty.")
        
        except KeyError as e:
            self.logger.exception(e)
            raise e("The shape does not exists.")
    
        return None