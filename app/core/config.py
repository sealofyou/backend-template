from typing import Optional, Any

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import AnyUrl


class Settings(BaseSettings):
    # 项目配置
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI Template"
    HOST: str = "127.0.0.1"
    PORT: int = 8000

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
    DB_URL: Optional[AnyUrl] = None
    DB_TEST_URL: Optional[AnyUrl] = None

    # Redis配置(按需启用)
    # REDIS_URL: Optional[AnyUrl] = None

    # modules ########################
    # 用户模块
    USE_USER_MODULE: bool = True

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
