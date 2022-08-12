import json
from redisgears import log

desc_json_p = {"name": 'P'}
GB("StreamReader", desc=json.dumps(desc_json_p)). \
    filter(lambda record: record['value']['dimension'] == 'P'). \
    foreach(lambda record: log(f'sandbox-p-{record}')). \
    register(
    prefix='ST:1MINUTE::::PG',
    convertToStr=True,
    collect=True,
    onFailedPolicy='abort',
    onFailedRetryInterval=1,
    batch=1,
    duration=0,
    trimStream=False)
log(f'Register P OK')
