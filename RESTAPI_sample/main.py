import os
from typing import Union, List
from enum import Enum
from fastapi import FastAPI, Query, Path, Body, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, HttpUrl
from models import IrisPrediction, ImagePrediction



class HtttpStatusCode(int, Enum):
    return_ok = 200
    return_not_found = 404
    return_internal_server_errot = 500

class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float



app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

iris_model = IrisPrediction()
image_model = ImagePrediction()

@app.post("/iris_prediction")
async def predict_iris_data(iris_data:IrisData):
    result = iris_model.predict_iris(
        iris_data.sepal_length,
        iris_data.sepal_width,
        iris_data.petal_length,
        iris_data.petal_width
    )
    return JSONResponse(content={"result": result})

@app.post("/image_prediction")
async def predict_image(image: UploadFile = File()):
    result = image_model.predict_image(image)
    return JSONResponse(content={"result": int(result)})






# @app.get("/sample2")
# async def get_sample2(q:Union[str, None]=Query(default=None,
#                                                max_length=50,
#                                                min_length=10,
#                                                pattern="^fixedquery$",
#                                                alias="qqq",
#                                                deplicated=True)):
#     return q

# @app.post("/soap")
# async def create_item(item: ItemRequest) -> ItemResponce:
#     return {"soap": item.soap, "order_code":[1,2,3,4,5], "order_name":["a","b","c","d","e"]}

# @app.get("/sample1")
# async def query_para(key: int = 0):
#     if key == 0:
#         return "you didn't define the key"
#     return f"you difined the key {key}"

# @app.get("/status/{httpstatuscode}")
# async def get_model(httpstatuscode: HtttpStatusCode):
#     if httpstatuscode is HtttpStatusCode.return_ok:
#         return {"httpstatuscode": httpstatuscode, "message": "OK"}

#     if httpstatuscode.value == 404:
#         return {"httpstatuscode": httpstatuscode, "message": "NOT FOUND!"}

#     if httpstatuscode.value == httpstatuscode.return_internal_server_errot:
#         return {"httpstatuscode": httpstatuscode, "message": "internal server error!"}

#     return {"httpstatuscode": httpstatuscode, "message": "hello error!"}

# @app.get("/{file_name:path}")
# async def get_file(file_name: str):
#     return os.path.join("統計学", file_name)

