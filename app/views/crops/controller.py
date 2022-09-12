from fastapi import  Depends, APIRouter
from .helper import getResult
from .schema import CropSchema

cropsRouter = APIRouter()

@cropsRouter.post('/result')
def call(data: CropSchema):
    return getResult(data)