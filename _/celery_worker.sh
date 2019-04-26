

nohup celery worker -A {celery_app} -P eventlet -l info >> logs/celery_worker.log 2>&1 &


# celery worker -A {celery_app} 和 celery worker -A {celery_task} 区别
# celery_app 可以执行默认注册的任务{可以没有默认任务}
# celery_task 除了加载了默认注册任务(引入celery.app实例缘故)，还可以执行celery_task的任务
#
# 异常：celery_app 启动时分配了没有注册的任务，会抛出执行异常

