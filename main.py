import time
from fastapi import FastAPI, Request

from app.core.config import settings
from app.utils.logger import LOGGER
from app.utils.businessexception import register_exception_handlers
from app.core.cors import CORSSetup
from app.modules.base.test import router as base_routers

app = FastAPI(title=settings.PROJECT_NAME)
# 注册异常处理
register_exception_handlers(app)
LOGGER.info("注册异常处理")

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

# 按需挂载路由
app.include_router(base_routers, prefix=settings.API_V1_STR + "/base")
# app.include_router(ml_routers.router, prefix=settings.API_V1_STR + "/ml")

# 按需挂载路由 此处可以通过config + if 判断是否挂载
# if settings.USE_USER_MODULE:
#     app.include_router(user_routers.router, prefix=settings.API_V1_STR + "/user")
app.include_router(base_routers.router, prefix=settings.API_V1_STR + "/base")

LOGGER.info("路由配置完成")


@app.get("/")
def root():
    return {"message": f"Welcome to {settings.PROJECT_NAME}"}


# 添加中间件判断程序运行时间
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time) + "s"
    return response


if __name__ == "__main__":
    import uvicorn

    try:
        # uvicorn.run(app, host=settings.HOST, port=settings.PORT)
        uvicorn.run("main:app", host=settings.HOST, port=settings.PORT, reload=True)
    except KeyboardInterrupt as e:
        print(f"{settings.API_V1_STR} 已关闭")
