from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# 始终定义 Base 类，即使数据库未配置
Base = declarative_base()

# 按需初始化数据库引擎和会话
if settings.USE_DATABASE and settings.DB_URL:
    engine = create_engine(settings.DB_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
else:
    SessionLocal = None


def get_db():
    """依赖注入的数据库会话"""
    if not SessionLocal:
        raise RuntimeError("Database not configured")

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()