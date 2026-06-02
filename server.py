import uvicorn
from fastapi import FastAPI, status
from pydantic import BaseModel
from shape_manager import ShapeManager

def manege_app():
    app = FastAPI()
    shape_manager = ShapeManager("shapes.json")

    @app.get("/shapes")
    def get_shapes():
        return shape_manager.get_all_shapes()

    @app.get("/shapes/{id}")
    def get_Shape_by_id(id:int):
        shape = shape_manager.find_shape_by_id(id)
        if shape:
            return shape.to_dict()
        else:
            
            return status.HTTP_404_NOT_FOUND

    uvicorn.run(app)


if __name__ == "__main__":
    manege_app()