from sys import prefix
from fastapi import Depends, APIRouter

from ..views.crops.controller import cropsRouter

router = APIRouter()

router.include_router(
    cropsRouter,
    prefix='/crops'
)