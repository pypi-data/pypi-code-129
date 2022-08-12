#!/usr/bin/python3.6
import sys
import pyodbc
import pandas as pd
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
        # super().__init__()
    
    def set(
        self,
        arrayName:str,
        key:str,
        value:str
    ):
        self.redis.hset(arrayName, key, value)

    def get(self, arrayName:str):
        return self.redis.hgetall(arrayName)

    def _getRedisClient(self):
        return self.redis

def getDataframe(query:str):
    try:
        df = pd.read_sql(query, con)
        return df
    except Exception as e:
        print(e)
        return None

def getCursorFromDatabase(
    server:str,
    database:str,
    username:str,
    password:str,
    driverLocation:str
):
    try:
        cnxn = pyodbc.connect(
            "DRIVER="+driverLocation+";"+
            "SERVER="+server+";"+
            "DATABASE="+database+";"+
            "UID="+username+";"+
            "PWD="+password+";"
        , timeout=5)
        return cnxn.cursor()
    except:
        print("Error on database connection")
        sys.exit(0)

def _fetchall(cursor:str, query:str):
    cursor.execute(query)
    rowAll = cursor.fetchall()
    return rowAll

def _fetchone(cursor:str, query:str):
    cursor.execute(query)
    row = cursor.fetchone()
    return row

def guessMetricByType(mainDict:dict, checkDict:dict):
    _arr = {}
    for i in checkDict:
        try:
            int(checkDict[i])
            mainDict[i] = 'count'
        except ValueError:
            mainDict[i] = 'string'

##validation method - This is only for Output validation purpose
def validatePluginData(result):
     obj,mandatory ={'Errors':""},['heartbeat_required','plugin_version']
     value={'heartbeat_required':["true","false",True,False],'status':[0,1]}
     for field in mandatory:
        if field not in result:
            obj['Errors']=obj['Errors']+"# Mandatory field "+field+" is missing #"
     for field,val in value.items():
        if field in result and result[field] not in val:
            obj['Errors']=obj['Errors']+"# "+field+" can only be "+str(val)
     if 'plugin_version' in result and not isinstance(result['plugin_version'],int):
        obj['Errors']=obj['Errors']+"# Mandatory field plugin_version should be an integer #"
     RESERVED_KEYS='plugin_version|heartbeat_required|status|units|msg|onchange|display_name|AllAttributeChart'
     attributes_List=[]
     for key,value in result.items():
         if key not in RESERVED_KEYS:
            attributes_List.append(key)
     if len(attributes_List) == 0:
        obj['Errors']="# There should be atleast one \"Number\" type data metric present #"
     if obj['Errors'] !="":
        obj['Result']="**************Plugin output is not valid************"
     else:
        obj['Result']="**************Plugin output is valid**************"
        del obj['Errors']
     result['validation output']= obj