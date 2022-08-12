# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Mike Zhou
# @Email : 公众号：测试开发技术
# @File : test_user_api_03.py

from API_Test_Project.fixture.user_api_fixture import *

class TestUserApi():

    def test_001_createUser(self,http,user_id,get_data):
        '''测试创建用户'''
        uri = '/api/users/{}'.format(user_id)
        globals()['user_id'] = user_id
        response = http.post(uri, data=json.dumps(get_data.get('playload')), headers=get_data.get('headers'))
        print(response.text)
        assert response.status_code == 201, '请求返回非201'

    def test_002_query_users(self,http, get_data):
        '''测试查询用户'''
        uri = '/api/users/{}'.format(globals()['user_id'])
        response = http.get(uri, data=json.dumps(get_data.get('playload')), headers=get_data.get('headers'))
        print(response.text)
        assert response.status_code == 200, '请求返回非200'
        assert json.dumps(get_data.get('playload')) in response.text

    def test_003_query_all_users(self,http,get_data):
        '''测试查询所有用户'''
        uri = '/api/users'
        response = http.get(uri, data=json.dumps(get_data.get('playload')), headers=get_data.get('headers'))
        print(response.text)
        count = response.json().get('count')
        items = response.json().get('items')
        assert response.status_code == 200, '请求返回非200'
        assert count == len(items)

    def test_004_update_users(self,http,get_data):
        '''测试更新用户'''
        uri = '/api/users/{}'.format(globals()['user_id'])
        self.playload = {'name': 'mikezhou_{}'.format(random.randint(1, 10))}
        response = http.put(uri, data=json.dumps(self.playload), headers=get_data.get('headers'))
        print(response.text)
        assert response.status_code == 200, '请求返回非200'
        assert json.dumps(self.playload) in response.text

    def test_005_delete_users(self,http,get_data):
        '''测试删除用户'''
        uri = '/api/users/{}'.format(globals()['user_id'])
        self.playload = {'name': 'mikezhou_{}'.format(random.randint(1, 10))}
        response = http.delete(uri, data=json.dumps(self.playload), headers=get_data.get('headers'))
        print(response.text)
        assert response.status_code == 200, '请求返回非200'

if __name__ == '__main__':
    pytest.main()