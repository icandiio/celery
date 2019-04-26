

nohup celery worker -A xcelery.app -P eventlet -l info >> logs/celery_worker.log 2>&1 &




# celery worker -A xcelery.app 和 celery worker -A xcelery.tasks.xtask 区别
# v1celery.app 可以执行默认注册的任务{可以没有默认任务}
# v1celery.tasks.xtask 除了加载了默认注册任务(引入celery.app实例缘故)，还可以执行xtask的任务
#
# 异常：v1celery.app 启动时分配了没有注册的任务，会抛出执行异常

