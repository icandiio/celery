from celery import Celery
from celery_dev import celery_config

"""
Celery库在使用前必须先实例化， 这个实例被称为application(或者简称为'app')
application是线程安全的，所以多个配置不同，组件和任务不同的实例可以同时存在于同一个进程空间。

宿主容器,运行时上下文环境
客户端和工作单元都会依赖宿主容器

角色 : 客户端(编程提交，定时任务< celery beat,只能启动一个实例 >)，工作单元端，中间人(队列)
"""

# celery 4.0 不再支持 windows

app = Celery("_dev_")  # 实例化

"""
celeryconfig.py

1.以加载文件导入
app.config_from_object("celeryconfig")

2.以配置模块导入
import celeryconfig
app.config_from_object(celeryconfig)

3.加载配置类/对象导入
class CeleryConfig:
    pass
app.config_from_object(Cofig)
"""
app.config_from_object(celery_config)

# app.conf.update({})

# @app.on_after_configure.connect # app 启动会自动回调有此装饰器的方法
# def setup_periodic_tasks(sender, **kwargs):
#     sender => app => celery 实例
#     sender.add_periodic_task(10, m1task.s(''), name="10 sec") # 可在项目中手动调用
