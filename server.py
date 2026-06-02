#TODO: change status code if not found. add pydantic

import uvicorn
from fastapi import FastAPI, status, Response
from pydantic import BaseModel
from shape_manager import ShapeManager

def manege_app():
    app = FastAPI()
    shape_manager = ShapeManager("shapes.json")

    @app.get("/shapes", status_code = 200)
    def get_shapes():
        return shape_manager.get_all_shapes()
        
    @app.get("/shapes/total-area")
    def get_total_area():
        total_area =  shape_manager.get_total_area()
        return total_area

    @app.get("/shapes/{id}")
    def get_Shape_by_id(id:int, response:Response):
        shape = shape_manager.find_shape_by_id(id)
        if shape:
            return shape.to_dict()
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
            return response.status_code

    @app.post("/shapes", status_code = 201)
    def add_a_shape(shape_dict:dict, response:Response):
        try:
            shape_object = shape_manager.create_shape(shape_dict)
            shape_manager.add_shape(shape_object)
            shape_manager.save_to_json()
        except (KeyError, ValueError) as e:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return response.status_code

    @app.put("/shapes/{id}", status_code = 200)
    def update_a_shape(id:int, new_data:dict, response:Response):
        try:
            shape = shape_manager.find_shape_by_id(id)
            shape_dict = shape.to_dict()
            is_updated = shape_manager.update_shape(shape_dict, new_data)
            if is_updated:
                shape_manager.shapes.remove(shape)
                shape_manager.save_to_json()
            else:
                response.status_code = status.HTTP_400_BAD_REQUEST
                return response.status_code
        except (KeyError, ValueError, TypeError) as e:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return response.status_code
    
    @app.delete("/shapes/{id}", status_code = 200)
    def delete_a_shape(id:int, response:Response):
        is_deleted = shape_manager.delete_shape(id)
        if not is_deleted:
            response.status_code = status.HTTP_404_NOT_FOUND
            return response.status_code
    
    uvicorn.run(app)


if __name__ == "__main__":
    manege_app()