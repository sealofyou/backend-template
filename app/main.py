from fastapi import FastAPI
from core.config import settings

from modules.base.test import router as base_routers
# from app.modules.ml import routers as ml_routers

app = FastAPI(title=settings.PROJECT_NAME)

# 按需挂载路由
app.include_router(base_routers, prefix=settings.API_V1_STR + "/base")
# app.include_router(ml_routers.router, prefix=settings.API_V1_STR + "/ml")


@app.get("/")
def root():
    return {"message": f"Welcome to {settings.PROJECT_NAME}"}

# 导入你的milvusus模块router
if settings.USE_MILVUS:
    # 这里按需导入
    # from modules.milvus.milvus_client import router as ml_router
    app.include_router(ml_router, prefix=settings.API_V1_STR + "/milvus")



if __name__ == "__main__":
    import uvicorn
    try:
        # uvicorn.run(app, host=settings.HOST, port=settings.PORT)
        uvicorn.run("main:app", host=settings.HOST, port=settings.PORT, reload=True)
    except KeyboardInterrupt as e:
        print(f"{settings.API_V1_STR} 已关闭")
