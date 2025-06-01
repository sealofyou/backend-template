# Fastapi 后端模板项目

## 项目目录结构
由于大部分模型调用方式，实现逻辑不同，这里考虑将其放弃，后续会考虑使用插件的方式来实现
1. requests调用
2. 路由添加，将其放到ml目录下。

```
fastapi-template/
├── app/
│   ├── core/                  # 核心配置和工具
│   │   ├── config.py
│   │   ├── security.py
│   │   └── dependencies.py
│   ├── modules/               # 功能模块
│   │   ├── base/              # 基础模块(用户管理)
│   │   │   ├── models.py
│   │   │   ├── schemas.py
│   │   │   ├── crud.py
│   │   │   ├── routers.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   │   ├── ml/                # 机器学习模块 具体看模型实现，这里只是 一个例子
│   │   │   ├── model_loader.py
│   │   │   ├── schemas.py
│   │   │   ├── routers.py
│   │   │   └── __init__.py
│   ├── db/                    # 数据库相关
│   │   ├── session.py
│   │   └── redis.py           # Redis连接(按需添加)
│   ├── utils/                 # 工具函数
│   │   └── logger.py
│   ├── main.py                # 应用入口
│   └── __init__.py
├── tests/                     # 测试目录
├── requirements.txt           # 依赖文件
├── .env                       # 环境变量
├── Dockerfile
└── README.md
```

