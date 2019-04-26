

nohup celery beat -A {celery_app} -l info >> logs/celery_beat.log 2>&1 &
