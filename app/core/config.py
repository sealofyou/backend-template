from typing import Optional, Any

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import AnyUrl
import os


class Settings(BaseSettings):
    # 项目配置
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI Template"
    HOST: str = "127.0.0.1"
    PORT: int = 8001
    WORKERS: int = 1 # 进程数

    # 跨域配置
    allow_origins: list[str] = ["*"]
    allow_credentials: bool = True
    allow_methods: list[str] = ["GET", "POST", "PUT", "DELETE"]
    allow_headers: list[str] = ["*"]

    # 日志配置
    LOG_NAME: str = "app"
    LOG_LEVEL: int = 20  # DEBUG = 10, INFO = 20, WARNING = 30, ERROR = 40, CRITICAL = 50
    LOG_WHEN: str = "D"
    LOG_BACKUP_COUNT: int = 5

    # 数据库配置(按需启用)
    # DB_URL: Optional[AnyUrl] = None
    # DB_TEST_URL: Optional[AnyUrl] = None

    # Redis配置(按需启用)
    # REDIS_URL: Optional[AnyUrl] = None


    # milvus 配置(按需启用)
    USE_MILVUS: bool = False
    MILVUS_HOST: str = os.getenv("MILVUS_HOST", "127.0.0.1")
    MILVUS_PORT: int = os.getenv("MILVUS_PORT", 19530)
    MILVUS_COLLECTION_NAME: str = os.getenv("MILVUS_COLLECTION_NAME", "test_collection")
    VECTOR_DIMENSION: int = os.getenv("VECTOR_DIMENSION", 768)
    METRIC_TYPE: str = os.getenv("METRIC_TYPE", "L2")

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
