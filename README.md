## 项目说明
 项目基于FastAPI开发，为后续模型相关服务开发实现节省时间
1. 服务开发放到modules中
2. 接口记得写：
   1. 装饰器中地址后面写：summary="接口名称", tags=["分类名"], response_model=返回格式
   2. 函数名下写："""段注释，可以生成，但尽可能全一些"""
   3. 原因：可以直接生成接口文档，apifox接口文档自动导入后看着会很舒服。
3. 模型相关函数放到ml中
4. logger使用：
```python
from app.utils.logger import logging

logging.info("hello world")
```

## 项目结构
```
fastapi-template/
├── app/
│   ├── core/                  # 核心配置和工具
│   │   ├── config.py
│   │   ├── security.py
│   │   └── dependencies.py
│   │   └── __init__.py
│   ├── modules/               # 功能模块 在这里添加
│   │   ├── models/            # pydantic 模型
│   │   └── __init__.py
│   ├── db/                    # 数据库相关 数据库/向量库
│   │   └── __init__.py
│   └── utils/                 # 工具函数
│       └── logger.py
├── tests/                     # 测试目录
├── main.py                    # 应用入口
├── requirements.txt           # 依赖文件
├── .env                       # 环境变量
├── Dockerfile
└── README.md
```
运行：
在根目录下执行： python main.py