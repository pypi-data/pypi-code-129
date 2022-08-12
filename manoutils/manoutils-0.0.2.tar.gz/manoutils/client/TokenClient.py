# -*- coding: utf-8 -*-
import logging

from manoutils.operator.RedisOperator import RedisOperator

logger = logging.getLogger(__name__)


class TokenClient(object):
    def __init__(self):
        self._opr = RedisOperator()
        self._redis_key = ""

    def getToken(self, exsysId, exsysType):
        self.setRedisKey(exsysId=exsysId, exsysType=exsysType)
        return self._opr.getString(self._redis_key)

    def setRedisKey(self, exsysId, exsysType):
        if exsysType.lower() == "oss":
            self._redis_key = "TOKEN_NFVO_2_{}_{}".format("cmoss".upper(), exsysId)
        else:
            self._redis_key = "TOKEN_NFVO_2_{}_{}".format(exsysType.upper(), exsysId)
