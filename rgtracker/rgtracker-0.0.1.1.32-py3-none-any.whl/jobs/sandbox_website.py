import json
from redisgears import log

desc_json_w = {"name": 'W'}
GB("StreamReader", desc=json.dumps(desc_json_w)). \
    filter(lambda record: record['value']['dimension'] == 'W'). \
    foreach(lambda record: log(f'sandbox-w-{record}')). \
    register(
    prefix='ST:1MINUTE:W:::PG',
    convertToStr=True,
    collect=True,
    onFailedPolicy='abort',
    onFailedRetryInterval=1,
    batch=1,
    duration=0,
    trimStream=False)
log(f'Register W OK')
