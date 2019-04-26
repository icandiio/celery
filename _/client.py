from xcelery.tasks import imports_task
from xcelery.tasks import xtask

"""
提交任务(编程式提交代码)
"""

# delay是apply_async的别名,返回AsyncResult实例
# imports_task.m1task.delay()
imports_task.s1task.delay()

# countdown second,延迟执行
# xtask.x1task.apply_async(countdown=5)
