## 项目说明

本项目基于FastAPI开发，为后续模型相关服务开发实现节省时间。

### 开发规范

1. 服务开发放到modules中
2. 接口记得写详细注释：
   1. 装饰器中地址后面写：summary="接口名称", tags=["分类名"], response_model=返回格式
   2. 函数名下写："""段注释，可以生成，但尽可能全一些"""
   3. 原因：可以直接生成接口文档，apifox接口文档自动导入后看着会很舒服。
3. 模型相关函数放到ml中
4. logger使用：
```python
from app.utils.logger import logging

logging.info("hello world")
```

### 项目结构

```
backend-template/
├── app/                       # 主应用目录
│   ├── core/                  # 核心配置和工具
│   │   ├── config.py          # 项目配置
│   │   ├── cors.py            # CORS配置
│   │   ├── fileConfig.py      # 文件配置
│   │   └── __init__.py
│   ├── dao/                   # 数据访问对象
│   │   ├── TestData.py
│   │   └── __init__.py
│   ├── db/                    # 数据库相关 数据库/向量库
│   │   ├── milvus.py
│   │   ├── redis.py
│   │   ├── session.py
│   │   └── __init__.py
│   ├── ml/                    # 机器学习模型相关
│   │   └── __init__.py
│   ├── modules/               # 功能模块 在这里添加
│   │   ├── base/              # 基础模块示例
│   │   │   ├── user/          # 用户相关功能
│   │   │   │   └── user.py
│   │   │   ├── crud.py
│   │   │   ├── models.py
│   │   │   ├── routers.py
│   │   │   ├── schemas.py
│   │   │   ├── test.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── utils/                 # 工具函数
│   │   ├── baseresponse.py
│   │   ├── businessexception.py
│   │   ├── globalexception.py
│   │   ├── logger.py
│   │   └── __init__.py
│   └── __init__.py
├── logs/                      # 日志文件目录
├── static/                    # 静态文件目录
│   └── swagger-ui/            # Swagger UI静态文件
├── main.py                    # 应用入口
├── pyproject.toml             # 项目配置和依赖管理
└── README.md                  # 项目说明文档
```

### 运行项目

#### 1. 环境配置

首先，复制环境变量示例文件并根据需要修改：

```bash
cp .env.example .env
```

#### 2. 创建虚拟环境

使用 `uv` 创建并激活虚拟环境：

```bash
# 创建虚拟环境
uv venv

# 激活虚拟环境 (Windows)
.venv\Scripts\activate

# 激活虚拟环境 (Linux/Mac)
# source .venv/bin/activate
```

#### 3. 安装依赖

```bash
uv sync
```

#### 4. 启动服务

##### 使用Python直接运行

```bash
python main.py
```

##### 使用Uvicorn运行（推荐用于生产环境）

```bash
uvicorn main:app --host 127.0.0.1 --port 8001
```

##### 使用Uvicorn运行（开发模式，支持热重载）

```bash
uvicorn main:app --host 127.0.0.1 --port 8001 --reload
```

### 依赖管理

本项目使用`uv`进行依赖管理：

#### 安装依赖

```bash
uv sync
```

#### 添加新依赖

```bash
uv add package-name
```

#### 添加开发依赖

```bash
uv add --dev package-name
```