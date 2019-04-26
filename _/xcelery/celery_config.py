"""
基本配置信息
"""
from datetime import timedelta

# 默认配置信息 => celery.app.defaults

mpath = "xcelery"

# 指定 Broker
broker_url = 'redis://tk:6379/1'

# 指定 Backend
result_backend = 'redis://tk:6379/2'

# 指定时区，默认是 UTC
timezone = 'Asia/Shanghai'

task_serializer = "json"

result_serializer = "json"

# 过滤数据
accept_content = ['json']

# #############################################################################
# 配置需要引入的任务执行模块，注册任务,()
# celery worker -A celery_app 初始加载的任务模块，worker执行的时候要验证任务模块的可执行性
imports = (
    # module name
    # 任务分模块主要是为了功能划分，便于管理
    '%s.tasks.imports_task' % mpath,
)

# schedule
# 启动周期性任务,即不需要调用方
beat_max_loop_interval = 30
beat_schedule = {
    # from celery.schedules import crontab
    # "schedule": crontab(minute="*/15"),
    #
    # from datetime import timedelta
    # 'schedule': timedelta(minutes=30),
    #
    # 'fixed_rate': {
    #     'task': '%s.tasks.v1task.m2tk' % mpath,
    #     'schedule': timedelta(seconds=30),  # 每 30 秒执行一次
    #     'args': (1,2,3),  # 任务函数参数
    #     'kwargs':{"k":"v"}
    # },
    # 'fixed_delay': {
    #     'task': '%s.tasks.v1task.m3tk' % mpath,
    #     'schedule': crontab(hour=9, minute=50),  # 每天早上 9 点 50 分执行一次
    #     'args': (3, ),  # 任务函数参数
    #     'options': {'queue': 'default'}
    # }
    'fixed_rate': {
        'task': '%s.tasks.imports_task.s1task' % mpath,
        'schedule': timedelta(seconds=10),  # 每 30 秒执行一次
        'args': (1,),  # 任务函数参数
        'kwargs': {"k": "v"}
    },
}
