# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : 狂师
# @Email : 公众号：测试开发技术
# @File : user_api_fixture.py

import random
import json
import hmac
import hashlib
import pytest
from API_Test_Project.common.http_requests import HttpRequests
from API_Test_Project.config.url_config import URLConf

@pytest.fixture(scope='function', autouse=True)
def http():
    url = URLConf.TEST_API_URL.value
    http = HttpRequests(url)
    return http

@pytest.fixture()
def get_parmas():
    device_sn = '123456789'
    os_platform = 'ios'
    app_version = '1.0'
    SECRET_KEY = "mikezhou"
    user_id = random.randint(10, 100)
    print(user_id)
    return locals()


@pytest.fixture(scope="function")
def get_token(http, get_parmas):
    '''获取token'''
    uri = '/api/get-token'
    headers = {'device_sn': get_parmas.get('device_sn'),
               'os_platform': get_parmas.get('os_platform'),
               'app_version': get_parmas.get('app_version'),
               'Content-Type': 'application/json'}

    args = (get_parmas.get('device_sn'), get_parmas.get('os_platform'), get_parmas.get('app_version'))
    content = ''.join(args).encode('ascii')
    sign_key = get_parmas.get('SECRET_KEY').encode('ascii')
    sign = hmac.new(sign_key, content, hashlib.sha1).hexdigest()
    data = {'sign': sign}
    response = http.post(uri, data=json.dumps(data), headers=headers)
    print(response.text)
    token = response.json().get('token')
    print(token)
    return token


@pytest.fixture()
def get_data(get_parmas, get_token):
    headers = {'device_sn': get_parmas.get('device_sn'),
               'token': get_token,
               'Content-Type': 'application/json'}
    playload = {'name': 'mikezhou'}
    return {'headers': headers, 'playload': playload}


@pytest.fixture()
def user_id(get_parmas):
    return get_parmas.get('user_id')

