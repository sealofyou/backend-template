from fastapi import APIRouter
from dao.TestData import Data
from utils.baseresponse import ResponseModel


router = APIRouter()

@router.get("/get/", summary="get测试接口", tags=["test"])
async def get_test(data: str):
    """
    此接口只用来进行get请求测试在开发时请删去
    """
    return ResponseModel.success(data)

@router.post("/post/{id}", summary="post测试接口", tags=["test"])
async def post_test(id:int, q:str | None = None, data: Data = None):
    """
    此接口只用来进行post请求测试在开发时请删去
    """
    res = {"id": id}
    if q: 
        res.update({"q": q})
    if data: 
        res.update({"data": data})
    return ResponseModel.success(res)
    