import sys
import types

from celery.utils.log import get_task_logger
from xcelery.app import app

logger = get_task_logger(__name__)

logger.info(sys.meta_path)


def module_from_code(code):
    module = types.ModuleType("_module_")
    exec(code, module.__dict__)
    return module


@app.task
def m1task(*args, **kwargs):
    code = kwargs.get("code", "")
    module = module_from_code(code)

    logger.info("++++++++m1tk+++++++++++")
