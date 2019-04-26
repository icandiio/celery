from pyx_gutils.util import conn_util

RedisConfs = {
    "host": "119.23.9.73",
    "port": 6379,
    "db": 7,
    "decode_responses": True,
    "password": "deliex-rds"
}

redis_cli = conn_util.get_redis_cli(**RedisConfs)
