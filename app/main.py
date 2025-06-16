from fastapi import FastAPI
from core.config import settings

from modules.base import routers as base_routers
from utils.logger import LOGGER
from utils.businessexception import register_exception_handlers
from utils.cors import CORSSetup

# from modules.ml import routers as ml_routers

app = FastAPI(title=settings.PROJECT_NAME)
# 注册异常处理
register_exception_handlers(app)
LOGGER.info("注册异常处理")

# 使用封装类配置 CORS
cors_setup = CORSSetup(
    app=app,
    allow_origins=settings.allow_origins,
    allow_credentials=settings.allow_credentials,
    allow_methods=settings.allow_methods,
    allow_headers=settings.allow_headers,
).setup()
LOGGER.info("CORS 配置完成")

# 按需挂载路由 此处可以通过config + if 判断是否挂载
# if settings.USE_USER_MODULE:
#     app.include_router(user_routers.router, prefix=settings.API_V1_STR + "/user")
app.include_router(base_routers.router, prefix=settings.API_V1_STR + "/base")
# app.include_router(ml_routers.router, prefix=settings.API_V1_STR + "/ml")
LOGGER.info("路由配置完成")


@app.get("/")
def root():

    return {"message": f"Welcome to {settings.PROJECT_NAME}"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
