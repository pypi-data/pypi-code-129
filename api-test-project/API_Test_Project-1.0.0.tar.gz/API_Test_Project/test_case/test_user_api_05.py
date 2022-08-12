# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Mike Zhou
# @Email : 公众号：测试开发技术
# @File : test_user_api_05.py

import os
from API_Test_Project.fixture.user_api_fixture import *
from API_Test_Project.common.parse_excel import *

def get_test_data():
    '''
    从外部获取参数数据
    :return:
    '''
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'test_data')
    excelPath = os.path.join(path, 'test_user_api_data.xlsx')
    print(excelPath)
    sheetName = '创建用户表'
    return ParseExcel(excelPath, sheetName)

@pytest.mark.test
class TestUserApi():

    @pytest.mark.mikezhou
    @pytest.mark.main
    @pytest.mark.parametrize('user_id,expect', get_test_data().getDatasFromSheet())
    def test_001_createUser(self,http,get_data,user_id,expect):
        '''测试创建用户'''
        print(user_id,expect)
        uri = '/api/users/{}'.format(user_id)
        response = http.post(uri, data=json.dumps(get_data.get('playload')), headers=get_data.get('headers'))
        print(response.text)
        status = response.json().get('success')
        assert response.status_code == 201, '请求返回非201'
        assert status == expect

    @pytest.mark.parametrize('user_id,expect', get_test_data().getDatasFromSheet())
    def test_002_query_users(self,http, get_data,user_id,expect):
        '''测试查询用户'''
        uri = '/api/users/{}'.format(user_id)
        response = http.get(uri, data=json.dumps(get_data.get('playload')), headers=get_data.get('headers'))
        print(response.text)
        assert response.status_code == 200, '请求返回非200'
        assert "get user success" in response.text

    @pytest.mark.mikezhou
    def test_003_query_all_users(self,http,get_data):
        '''测试查询所有用户'''
        uri = '/api/users'
        response = http.get(uri, data=json.dumps(get_data.get('playload')), headers=get_data.get('headers'))
        print(response.text)
        count = response.json().get('count')
        items = response.json().get('items')
        assert response.status_code == 200, '请求返回非200'
        assert count == len(items)

    @pytest.mark.parametrize('user_id,expect', get_test_data().getDatasFromSheet())
    def test_004_update_users(self,http,get_data,user_id,expect):
        '''测试更新用户'''
        uri = '/api/users/{}'.format(user_id)
        self.playload = {'name': 'mikezhou_{}'.format(random.randint(1, 10))}
        response = http.put(uri, data=json.dumps(self.playload), headers=get_data.get('headers'))
        print(response.text)
        assert response.status_code == 200, '请求返回非200'
        assert "update success" in response.text

    @pytest.mark.mikezhou
    @pytest.mark.parametrize('user_id,expect', get_test_data().getDatasFromSheet())
    def test_005_delete_users(self,http,get_data,user_id,expect):
        '''测试删除用户'''
        uri = '/api/users/{}'.format(user_id)
        self.playload = {'name': 'mikezhou_{}'.format(random.randint(1, 10))}
        response = http.delete(uri, data=json.dumps(self.playload), headers=get_data.get('headers'))
        print(response.text)
        assert response.status_code == 200, '请求返回非200'
        assert "delete success" in response.text

if __name__ == '__main__':
    pytest.main()