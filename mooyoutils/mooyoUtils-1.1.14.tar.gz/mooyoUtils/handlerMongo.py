# -*- coding: UTF-8 -*-
# @Time     : 2020/7/10 10:22
# @Author   : Jackie
# @File     : handlerMongo.py
from .logger import logger
import pymongo
from read_config import apollo_reader


class MongoHandler:
    def __init__(self, conn_config=None, tag=None):
        """

        :param conn_config: mongo的链接信息
        :param tag: 根据tag 获取 Apollo 中的配置信息
        """
        if conn_config:
            self.conn_config = conn_config
        else:
            self.conn_config = apollo_reader.get_value(f'mongo.{tag}.config')
        if not self.conn_config:
            raise RuntimeError(f'MongoHandler初始化错误，请确认conn_config:{conn_config} or tag:{tag}.')
        self.client = self.init_client()
        self.dbs = {}
        self.coll_list = {}

    def init_client(self):
        self.client = pymongo.MongoClient(self.conn_config)
        logger.info(f'MongoClient conn success. {self.client}')
        return self.client

    def get_dbs(self):
        # 获取mongo下所有的 db
        return self.client.list_database_names()

    def get_db(self, db_name):
        # 根据db_name 获取 db 实例
        if db_name in self.dbs:
            return self.dbs[db_name]['obj']
        db = self.client.get_database(db_name)
        self.dbs[db_name] = {}
        self.dbs[db_name]['obj'] = db
        return db

    def get_collections(self, db_name):
        # 获取 db 下 所有的collection
        return self.get_db(db_name).list_collection_names()

    def get_coll(self, db_name, coll_name):
        # 根据 coll_name 获取 collection 实例
        db = self.get_db(db_name)
        db_data = self.dbs[db_name]
        if coll_name in db_data:
            return db_data[coll_name]
        coll = db[coll_name]
        db_data[coll_name] = coll
        return coll

    def get_result(self, db_name, coll_name, params, *args, **kwargs):
        # 根据 条件进行查询
        logger.info(f'Query mongo: db_name:{db_name}, coll_name:{coll_name}, params:{args, kwargs}')
        coll = self.get_coll(db_name, coll_name)
        return list(coll.find(params, *args, **kwargs))

    def close(self):
        if self.client:
            self.close()

    def __enter__(self):
        if not self.client:
            self.init_client()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        logger.info(f'db [{self.conn_config}] close...exc_type:{exc_type}, exc_val:{exc_val}, exc_tb:{exc_tb}.')
        self.close()
