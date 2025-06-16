from fastapi import APIRouter
from dao.TestData import Data
from utils.baseresponse import ResponseModel


router = APIRouter()

@router.get("/get/")
async def get_test(data: str):
    return ResponseModel.success(data)

@router.post("/post/{id}")
async def post_test(id:int, q:str | None = None, data: Data = None):
    res = {"id": id}
    if q: 
        res.update({"q": q})
    if data: 
        res.update({"data": data})
    return ResponseModel.success(res)
    