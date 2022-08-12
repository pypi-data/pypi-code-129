# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : 狂师
# @Email : 公众号：测试开发技术
# @File : run_testcase_by_tag.py


import pytest

# 定义标签，按照指定标签过滤运行用例
tag = "mikezhou"
pytest.main(["-v","-s","-m", f"{tag}","--collect-only"])