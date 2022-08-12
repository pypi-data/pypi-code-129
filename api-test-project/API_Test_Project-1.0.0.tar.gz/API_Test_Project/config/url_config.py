# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Mike Zhou
# @Email : 公众号：测试开发技术
# @File : url_config.py


import enum

class URLConf(enum.Enum):
    '''
    环境配置枚举类
    '''
    TEST_API_URL = 'http://127.0.0.1:5000/'
    PROD_API_URL = 'http://www.stp.com/'

if __name__ == '__main__':
    print(URLConf.TEST_API_URL.name)
    print(URLConf.TEST_API_URL.value)