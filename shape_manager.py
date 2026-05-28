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
    
    def create_shape(self, shape:dict) -> object | None:
        """docstring"""
        try:
            return SHAPE_CLASSES[shape["type"]](**shape)
        
        except KeyError as e:
            raise e("The shape type does not exists.")
        

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
                self.shapes.append(self.create_shape(shape_dict))
                Shape.counter -= 1 
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

    def save_to_json(self, json_file_path:str):
        """docstring"""
        is_saved = False
        shapes_list = self.get_all_shapes()
        
        with open(json_file_path, "w") as f:
            json.dump(shapes_list)
        
        is_saved = True

        return is_saved

        

    def load_from_json(self, json_file_path:str) -> None:
        """docstring"""
        try:
            with open(json_file_path, "r") as f:
                list_shapes_dicts = json.load(f)
        
        except json.decoder.JSONDecodeError as e:
            self.logger.exception("the json file is empty.")
            print("the json file is empty.")
        
        else:
            for shape in list_shapes_dicts:
                self.shapes.append(self.create_shape(shape))

        return None