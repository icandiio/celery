# cmd.py 是系统自带module，不能重名


if __name__ == '__main__':
    from celery.bin.celery import main

    # main("celery worker -A xcelery.app".split())
    main("celery beat -A xcelery.app".split())
