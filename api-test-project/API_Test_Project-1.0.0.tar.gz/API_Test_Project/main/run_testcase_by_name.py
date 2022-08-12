# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : 狂师
# @Email : 公众号：测试开发技术
# @File : run_testcase_by_name.py


import pytest

# 定义表达式运行含有指定的关键字名称的测试用例
name = "user"
pytest.main(["-v","-s","-k", f"{name}"])
