#!/usr/bin/python3.6
import sys
import json
import pyodbc
import re
import redis

'''Author: Peter Malaty
   Author2: Renas Mirkan Kilic
   Date: Nov 06/2020
'''

'''Monitor Global Vars'''
GlobalSelector = '24'

def addToRedis(con,arrayName,key,value):
    con.hset(arrayName, key, value)

def getFromRedis(con,arrayName):
    return con.hgetall(arrayName)

RedisInst = redis.Redis(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True)

labelUse = re.sub('\s+','',str(getFromRedis(RedisInst,GlobalSelector)['label']))


dictArray = {}


for i in getFromRedis(RedisInst,GlobalSelector):
    #print(str(i) + '---' + getFromRedis(RedisInst,GlobalSelector)[i])
    if i == 'label' or i == 'membership_plan_id':
        continue
    if str(getFromRedis(RedisInst,GlobalSelector)[i]) == 'None' or str(getFromRedis(RedisInst,GlobalSelector)[i]) == 'Nulll':
        dictArray[i] = '0'
    else:
        dictArray[i] = getFromRedis(RedisInst,GlobalSelector)[i]


PLUGIN_VERSION = "2"

HEARTBEAT = "true"

PROC_FILE = "/proc/sys/fs/file-nr"

METRIC_UNITS = {}
for y in dictArray:
    METRIC_UNITS[y] = 'count'

    

def metricCollector():
    data = {}
    data['plugin_version'] = PLUGIN_VERSION
    data['heartbeat_required'] = HEARTBEAT
    data['Author'] = 'Renas Mirkan Kilic'
    data['DateCreated'] = 'Nov 6th, 2020'
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
