from celery.app.task import Task
from celery.utils.log import get_task_logger
from xcelery.app import app

"""
定义任务, 注册任务（config） 和 提交任务（提交任务的方式）

1. define task

    @app.task                   #注册任务
    def func(*args,**kwargs):   #定义任务
        pass

2. exec task or submit task（异步任务和定时任务）
    1.func.delay(*args,**kwargs) # 2 的简写方式
    2.func.apply_async((*args,**kwargs),...)
    3.周期性调度 {celery beat}
"""

logger = get_task_logger(__name__)


@app.task
def s1task(*args, **kwargs):
    logger.info(args);
    logger.info(kwargs);
    logger.info("++++++++s1tk+++++++++++")


class MyTask(Task):

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        logger.info("+++++failure++++++++")

    def on_success(self, retval, task_id, args, kwargs):
        logger.info("+++++success++++++++")


@app.task(base=MyTask)
def m1task(*args, **kwargs):
    logger.info("++++++++m1task+++++++++++")
