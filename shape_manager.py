import json
from square import Square
from rectangle import Rectangle
from circle import Circle

class ShapeManager:
    """docstring"""
    def __init__(self) -> None:
        """docstring"""
        self.shapes = []
        self.load_from_json()
    
    def create_shape(self, shape:dict) -> object | None:
        """docstring"""
        match shape["type"]:
            case "circle":
                return Circle(**shape)
            case "square":
                return Square(**shape)
            case "rectangle":
                return Rectangle(**shape)
        
        return None

    def get_all_shapes(self) -> list:
        """docstring"""
        shapes_list = []
        
        for shape in self.shapes:
            shapes_list.append(shape.to_dict())
        
        return shapes_list
    
    def update_shape(self, shape_id:str, new_data:dict) -> bool:
        """docstring"""
        is_updated = False
        for shape in self.shapes:
            if shape.id == shape_id:
                shape_dict = shape.to_dict()
                shape_dict.update(shape_id, **new_data)
                self.shapes.remove(shape)
                self.shapes.append(self.create_shape(shape_dict))
                is_updated = True 
        
        return is_updated
    
    def delete_shape(self, shape_id:str) -> bool:
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
        with open(json_file_path, "r") as f:
            list_shapes_dicts = json.load(f)
            
            for shape in list_shapes_dicts:
                self.shapes.append(self.create_shape(shape))

        return None