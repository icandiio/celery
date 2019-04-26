# cmd.py 是系统自带module，不能重名


def _cmd():
    from celery.bin.celery import main

    # 通过命令行运行
    # main("celery worker -A xcelery.app".split())
    main("celery beat -A xcelery.app -l info".split())


def _app():
    # 通过 celery 来运行 ，最终会转为命令行运行
    from xcelery.app import app
    app.start("celery beat -l info ".split())


if __name__ == '__main__':
    _app()
    import time

    while True:
        print("=====")
        time.sleep(10)
    pass
