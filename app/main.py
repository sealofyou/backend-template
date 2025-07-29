import time
from fastapi import FastAPI, Request
from core.cors import CORSSetup
from utils.businessexception import register_exception_handlers
from core.config import settings
from utils.logger import LOGGER

from modules.base import routers as base_routers
from utils.logger import LOGGER
from utils.businessexception import register_exception_handlers
from core.cors import CORSSetup
from modules.base.test import router as base_routers
<<<<<<< HEAD
=======

>>>>>>> 3aae2fa7be90b7406884c181d17789549d9e0c9c

app = FastAPI(title=settings.PROJECT_NAME)
# 注册异常处理
register_exception_handlers(app)
LOGGER.info("注册异常处理")

<<<<<<< HEAD
# 注册异常处理
register_exception_handlers(app)
LOGGER.info("注册异常处理")
=======
>>>>>>> 3aae2fa7be90b7406884c181d17789549d9e0c9c
# 使用封装类配置 CORS
cors_setup = CORSSetup(
    app=app,
    allow_origins=settings.allow_origins,
    allow_credentials=settings.allow_credentials,
    allow_methods=settings.allow_methods,
    allow_headers=settings.allow_headers,
).setup()
LOGGER.info("CORS 配置完成")

<<<<<<< HEAD
# 按需挂载路由
app.include_router(base_routers, prefix=settings.API_V1_STR + "/base")
# app.include_router(ml_routers.router, prefix=settings.API_V1_STR + "/ml")
=======
# 按需挂载路由 此处可以通过config + if 判断是否挂载
# if settings.USE_USER_MODULE:
#     app.include_router(user_routers.router, prefix=settings.API_V1_STR + "/user")
app.include_router(base_routers.router, prefix=settings.API_V1_STR + "/base")

LOGGER.info("路由配置完成")
>>>>>>> 3aae2fa7be90b7406884c181d17789549d9e0c9c


@app.get("/")
def root():
    return {"message": f"Welcome to {settings.PROJECT_NAME}"}

# 导入你的milvusus模块router
if settings.USE_MILVUS:
    # 这里按需导入
    from modules.milvus.milvus_client import router as ml_router
    app.include_router(ml_router, prefix=settings.API_V1_STR + "/milvus")


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
