# coding:utf-8

"""

# app = Celer(broker,backend)，装饰器，配置信息，流程化操作，控制消息的发送和接收
# 消息:任务序列化文本
# broker{rabbitmq,redis}。producer->broker->storage->broker->consumer
# backend,执行结果存储

# 异步任务
# client,生成任务
# 任务:app装饰器修饰函数

# 定时任务
# 启动定时任务调度器（调度器实例只应该启动一个）
# celery beat

# 消费端
# 启动一个worker实例，监控任务队列是否有任务需要处理
# 任务:app装饰器修饰函数



# 启动worker
celery worker -A module -l info
celery worker --help
# 启动worker,同时启动定时任务调度器
celer worker -A module -B -l info




组件：序列化{格式{pickle,json,yaml},压缩，加密}，并发{gevent,eventlet,进程/线程}


远程控制:在运行时用 celery inspect 和 celery control 命令检视和管理职程的能力



"""
