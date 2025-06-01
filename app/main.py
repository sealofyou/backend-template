from fastapi import FastAPI
from app.core.config import settings

from app.modules.base import routers as base_routers
# from app.modules.ml import routers as ml_routers

app = FastAPI(title=settings.PROJECT_NAME)

# 按需挂载路由
app.include_router(base_routers.router, prefix=settings.API_V1_STR + "/base")
# app.include_router(ml_routers.router, prefix=settings.API_V1_STR + "/ml")


@app.get("/")
def root():

    return {"message": f"Welcome to {settings.PROJECT_NAME}"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
