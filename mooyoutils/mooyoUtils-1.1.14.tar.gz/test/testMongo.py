# -*- coding: UTF-8 -*-
# @Time     : 2022/6/23 13:35
# @Author   : Jackie
# @File     : testMongo.py
from mooyoUtils.handlerMongo import MongoHandler


if __name__ == '__main__':
    m = MongoHandler('mongodb://root:5T8JbklD9v5ylAZ@s-d9j40f279e3cd0c4.mongodb.ap-southeast-5.rds.aliyuncs.com:3717,s-d9jc65211d9803b4.mongodb.ap-southeast-5.rds.aliyuncs.com:3717/sdk-backend?authSource=admin')
    print(m.client.get_database('userData'))
    r = m.get_result('userData', 'user', {'user_id': 3800823})
    # for k, v in r[0].items():
    #     if isinstance(v, dict):
    #         print(k, '---->', len(v), v.values())
    #     else:
    #         print(k, '---->', v)
    dbs = m.client.list_database_names()
    for db_name in dbs:
        db = m.get_db(db_name)
        tb = db.list_collection_names()
        print(db_name, tb)
