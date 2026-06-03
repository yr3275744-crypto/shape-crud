#TODO: change status code if not found. add pydantic. add logs.

import uvicorn
from fastapi import FastAPI, HTTPException
from shape_manager import ShapeManager
import logger_setup

def manege_app():
    """dmanag an fastapi app to manege shape"""
    app = FastAPI()
    shape_manager = ShapeManager("shapes.json")
    logger = logger_setup.create_manage_shape_logger()

    @app.get("/shapes", status_code = 200)
    def get_shapes():
        """send all shapes list"""
        logger.info("send all shapes now")
        return shape_manager.get_all_shapes()
        
    @app.get("/shapes/total-area")
    def get_total_area():
        """send the total area of all the shapes."""
        total_area =  shape_manager.get_total_area()
        logger.info("send total area now")
        return total_area

    @app.get("/shapes/{id}")
    def get_Shape_by_id(id:int):
        """send a specific shape by its id"""
        shape = shape_manager.find_shape_by_id(id)
        if shape:
            logger.info("send shape now")
            return shape.to_dict()
        else:
            logger.error("Failed to send shape. The shape id does not exists")
            raise HTTPException(status_code = 404, detail = "The shape id does not exists")
            

    @app.post("/shapes", status_code = 201)
    def add_a_shape(shape_dict:dict):
        """add a shape."""
        try:
            shape_object = shape_manager.create_shape(shape_dict)
            shape_manager.add_shape(shape_object)
            shape_manager.save_to_json()
        
        except (KeyError, TypeError) as e:
            logger.error("adding shape is faild.")
            logger.exception(e)
            raise HTTPException(status_code = 400, detail = "Invalid key.")
        
        except ValueError as e:
            logger.error("adding shape is faild.")
            logger.exception(e)
            raise HTTPException(status_code = 400, detail = "Invalid value.")
            

    @app.put("/shapes/{id}", status_code = 200)
    def update_a_shape(id:int, new_data:dict):
        """update a shape."""
        try:
            shape = shape_manager.find_shape_by_id(id)
            shape_dict = shape.to_dict()
            is_updated = shape_manager.update_shape(shape_dict, new_data)
            if is_updated:
                shape_manager.shapes.remove(shape)
                shape_manager.save_to_json()
                logger.info("The shape is updated successfully.")
            else:
                logger.error("The shape update is failed. The shape does not exists.")
                raise HTTPException(status_code = 404, detail = "The shape does not found")
       
        except (KeyError, TypeError) as e:
            logger.error("The shape update is failed")
            logger.exception(e)
            raise HTTPException(status_code = 400, detail = "Invalid data.")
        
        except ValueError as e:
            logger.error("The shape update is failed")
            logger.exception(e)
            raise HTTPException(status_code = 404, detail = "Invalid value")
    
    @app.delete("/shapes/{id}", status_code = 200)
    def delete_a_shape(id:int):
        """delet a shape."""
        is_deleted = shape_manager.delete_shape(id)
        if not is_deleted:
            logger.error("The removeing shape failed. The shape does not exists")
            raise HTTPException(status_code = 404, detail = "The shape does not found")
        logger.info("The shape is deleted successfully.")
    
    uvicorn.run(app)


if __name__ == "__main__":
    manege_app()