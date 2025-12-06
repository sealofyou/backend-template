from typing import Optional
from pydantic import BaseModel, EmailStr


# 用户创建模型
class UserCreate(BaseModel):
    email: EmailStr
    password: str


# 用户更新模型
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None


# 用户返回模型
class UserOut(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes = True
