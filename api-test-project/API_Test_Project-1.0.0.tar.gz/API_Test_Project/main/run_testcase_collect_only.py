# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : 狂师
# @Email : 公众号：测试开发技术
# @File : run_testcase_collect_only.py


import pytest

# 仅收集测试用例数量，不运行用例
if __name__ == '__main__':
    pytest.main(["--collect-only"])