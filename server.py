import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from shape_manager import ShapeManager

def manege_app():
    app = FastAPI()
    shape_manager = ShapeManager("shapes.json")


    @app.get("/shapes")
    def get_shapes():
        return shape_manager.get_all_shapes()


    uvicorn.run(app)


if __name__ == "__main__":
    manege_app()