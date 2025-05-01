from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/products", tags=["products"], responses={404: {"description": "Not found"}})

products_list = ["producto1", "producto2", "producto3", "producto4", "producto5"]



@router.get("/")
async def products():
    return products_list


@router.get("/{id}")
async def products(id: int):
    return products_list[id]