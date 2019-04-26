from celery.utils.log import get_task_logger
from celery_dev.celery_app import app

logger = get_task_logger(__name__)


@app.task
def x1task(*args, **kwargs):
    logger.info("++++++++x1task+++++++++++")
