from typing import Optional, Any

from pydantic import BaseModel
from utils.businessexception import ErrorCode


# 统一响应模型
class ResponseModel(BaseModel):
    code: int
    message: str
    data: Optional[Any] = None  # 默认为 None

    @classmethod
    def success(cls, data: Any = None, message: str = None):
        return cls(
            code=ErrorCode.SUCCESS.code,
            message=message or ErrorCode.SUCCESS.message,  # 可选自定义消息
            data=data
        )

    @classmethod
    def error(cls, error_code: ErrorCode, message: str = None, data: Any = None):
        return cls(
            code=error_code.code,
            message=message or error_code.message,  # 优先使用传入 message
            data=data  # 可选传入 data
        )