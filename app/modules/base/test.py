from typing import Annotated
from fastapi import APIRouter, Depends, File, UploadFile
from fastapi.security import OAuth2PasswordBearer
from app.utils.baseresponse import ResponseModel
from app.utils.logger import logging


router = APIRouter()

@router.get("/get/", summary="get测试接口", tags=["test"])
async def get_test(data: str):
    """
    此接口只用来进行get请求测试在开发时请删去
    """
    return ResponseModel.success(data)

@router.post("/post/{id}", summary="post测试接口", tags=["test"])
async def post_test(id:int, q:str | None = None, data: dict = None):
    """
    此接口只用来进行post请求测试在开发时请删去
    """
    res = {"id": id}
    if q: 
        res.update({"q": q})
    if data: 
        res.update({"data": data})
    return ResponseModel.success(res)

@router.post("/file/", summary="上传文件测试接口", tags=["test"])
async def file_test(file: bytes = File()):
    """
    此接口只用来进行上传文件测试在开发时请删去
    该接口以bytes形式接收和读取文件内容适用于小型文件
    """
    return {"file_size": len(file)}

@router.post("/uploadfile/", summary="优先采用上传文件测试接口", tags=["test"])
async def upload_file_test(file: UploadFile):
    """
    此接口只用来进行上传文件测试在开发时请删去
    该接口以UploadFile形式接收和读取文件内容适用于*所有文件*
    """
    return ResponseModel.success({"filename": file.filename, "content_type": file.content_type})

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
@router.get("/items/")
async def read_items(token: Annotated[str| None, Depends(oauth2_scheme)]):
    return {"token": token}
