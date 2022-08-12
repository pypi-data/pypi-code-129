import json
from redisgears import log

desc_json_s = {"name": 'S'}
GB("StreamReader", desc=json.dumps(desc_json_s)). \
    filter(lambda record: record['value']['dimension'] == 'S'). \
    foreach(lambda record: log(f'sandbox-s-{record}')). \
    register(
    prefix='ST:1MINUTE::::PG',
    convertToStr=True,
    collect=True,
    onFailedPolicy='abort',
    onFailedRetryInterval=1,
    batch=1,
    duration=0,
    trimStream=False)
log(f'Register S OK')
