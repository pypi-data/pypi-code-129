#!/usr/bin/python3.6
import sys
import json
import re
import redis

class redisClient:
    def __init__(self,host,port,db,charset="utf-8",decode_responses=True):
        self.host=host
        self.port=port
        self.db=db
        self.charset=charset
        self.decode_responses=decode_responses
        self.redis=redis.Redis(
            host=self.host,
            port=self.port,
            db=self.db,
            charset=self.charset,
            decode_responses=self.decode_responses
        )
    
    def _set(
        self,
        arrayName:str,
        key:str,
        value:str
    ):
        self.redis.hset(arrayName, key, value)

    def get(self, arrayName:str):
        return self.redis.hgetall(arrayName)

RedisInst = redisClient(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True)

'''Monitor Global Vars'''
GlobalSelector = 'pr_payment_transaction_creditcard_card_type_9'
cardTypeAP = 'AP'
dictArray = {}

for i in RedisInst.get(GlobalSelector):
    if re.match('.*store_group_name.*', i) or re.match('.*store_group_id.*', i) or re.match('.*card_type.*', i):
        continue
    if str(RedisInst.get(GlobalSelector)[i]) == 'None' or str(RedisInst.get(GlobalSelector)[i]) == 'Nulll':
        dictArray[i] = '0'
    else:
        # tranType = str(i).split('@')[0]
        brand = str(i).split('@@@')[0]
        metricMeasure = str(i).split('@@@')[1]
        cardType = str(i).split('@@@')[2]
        print(brand + ' ' + metricMeasure + ' ' + cardType)
        if cardTypeAP == 'AP':
            if re.match('ap_.*', cardType):
                dictArray[brand + '_' + metricMeasure + '_' + cardType] = str(RedisInst.get(GlobalSelector)[i])
            else:
                continue
        else:
            if not re.match('ap_.*', cardType):
                dictArray[brand + '_' + metricMeasure + '_' + cardType] = str(RedisInst.get(GlobalSelector)[i])
            else:
                continue

# PLUGIN FUNCTION CALL
PLUGIN_VERSION = "4"

HEARTBEAT = "true"

def guessMetricByType(mainArr:dict, checkArr:dict):
    _arr = {}
    for i in checkArr:
        try:
            int(checkArr[i])
            mainArr[i] = 'count'
        except ValueError:
            mainArr[i] = 'string'
    return 1

METRIC_UNITS = {}
guessMetricByType(METRIC_UNITS, dictArray)

def metricCollector():
    data = {}
    data['plugin_version'] = PLUGIN_VERSION
    data['heartbeat_required'] = HEARTBEAT
    data['descripton'] = "tx: fail, decline, approve | visa, mastercard, discover"

    try:
        data["units"] = METRIC_UNITS

        for x in dictArray:
            data[x] = dictArray[x]

    except Exception as e:
        data["error"] = str(e)
    return data

if __name__ == "__main__":
    result = metricCollector()
    print(json.dumps(result, indent=4, sort_keys=False))
