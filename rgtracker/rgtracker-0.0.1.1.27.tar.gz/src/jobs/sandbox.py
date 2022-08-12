from redisgears import log

GB("StreamReader"). \
    filter(lambda record: record['value']['dimension'] == 'P'). \
    foreach(lambda record: log(f'{record}')). \
    run('ST:1MINUTE::::PG', trimStream=False)
