

nohup celery beat -A xcelery.app -l info >> logs/celery_beat.log 2>&1 &
