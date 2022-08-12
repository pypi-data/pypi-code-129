# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Mike Zhou
# @Email : 公众号：测试开发技术
# @File : test_user_api_02.py

import random
import hmac
import hashlib
import json
import pytest
from API_Test_Project.common.http_requests import HttpRequests
from API_Test_Project.config.url_config import URLConf


class TestUserApi():

    def setup_class(cls) -> None:
        cls.url = URLConf.TEST_API_URL.value
        cls.http = HttpRequests(cls.url)
        cls.device_sn = '123456789'
        cls.os_platform = 'ios'
        cls.app_version = '1.0'
        cls.SECRET_KEY = "mikezhou"
        cls.user_id = random.randint(10, 100)
        print(cls.user_id)

    def setup(self) -> None:
        self.headers = {'device_sn': TestUserApi.device_sn,
                        'token': TestUserApi.get_token(),
                        'Content-Type': 'application/json'}
        self.playload = {'name': 'mikezhou'}

    @staticmethod
    def get_token():
        '''获取token'''
        uri = '/api/get-token'
        headers = {'device_sn': TestUserApi.device_sn,
                   'os_platform': TestUserApi.os_platform,
                   'app_version': TestUserApi.app_version,
                   'Content-Type': 'application/json'}

        args = (TestUserApi.device_sn, TestUserApi.os_platform, TestUserApi.app_version)
        content = ''.join(args).encode('ascii')
        sign_key = TestUserApi.SECRET_KEY.encode('ascii')
        sign = hmac.new(sign_key, content, hashlib.sha1).hexdigest()
        data = {'sign': sign}
        response = TestUserApi.http.post(uri, data=json.dumps(data), headers=headers)
        print(response.text)
        token = response.json().get('token')
        print(token)
        return token

    def test_001_createUser(self):
        '''测试创建用户'''
        uri = '/api/users/{}'.format(TestUserApi.user_id)
        response = TestUserApi.http.post(uri, data=json.dumps(self.playload), headers=self.headers)
        print(response.text)
        assert response.status_code == 201, '请求返回非201'

    def test_002_query_users(self):
        '''测试查询用户'''
        uri = '/api/users/{}'.format(TestUserApi.user_id)
        response = TestUserApi.http.get(uri, data=json.dumps(self.playload), headers=self.headers)
        print(response.text)
        assert response.status_code == 200, '请求返回非200'
        assert json.dumps(self.playload) in response.text

    def test_003_query_all_users(self):
        '''测试查询所有用户'''
        uri = '/api/users'
        response = TestUserApi.http.get(uri, data=json.dumps(self.playload), headers=self.headers)
        print(response.text)
        count = response.json().get('count')
        items = response.json().get('items')
        assert response.status_code == 200, '请求返回非200'
        assert count == len(items)

    def test_004_update_users(self):
        '''测试更新用户'''
        uri = '/api/users/{}'.format(TestUserApi.user_id)
        self.playload = {'name': 'mikezhou_{}'.format(random.randint(1, 10))}
        response = TestUserApi.http.put(uri, data=json.dumps(self.playload), headers=self.headers)
        print(response.text)
        assert response.status_code == 200, '请求返回非200'
        assert json.dumps(self.playload) in response.text

    def test_005_delete_users(self):
        '''测试删除用户'''
        uri = '/api/users/{}'.format(TestUserApi.user_id)
        self.playload = {'name': 'mikezhou_{}'.format(random.randint(1, 10))}
        response = TestUserApi.http.delete(uri, data=json.dumps(self.playload), headers=self.headers)
        print(response.text)
        assert response.status_code == 200, '请求返回非200'


if __name__ == '__main__':
    pytest.main()