# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : 小易
# @File : run_test_allure.py
# @Project : webuitestpythonProject

import time
import os
import pytest
import warnings
from py.xml import html
from UI_Test_Project.common.browser import Browser
import allure

_driver = None

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """当测试失败的时候，自动截图，展示到html报告中"""
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    report.description = str(item.function.__doc__)
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")  # 设置编码显示中文

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))

def _capture_screenshot():
    '''截图保存为base64'''
    print(_driver)
    return _driver.get_screenshot_as_base64()

@pytest.fixture(scope='session',autouse=True)
def driver():
    global _driver
    warnings.simplefilter('ignore', ResourceWarning)
    _driver = Browser.open_browser('chrome')
    yield _driver
    time.sleep(2)
    _driver.quit()


_driver = None

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    获取每个用例状态的钩子函数
    :param item:
    :param call:
    :return:
    '''
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # 添加allure报告截图
        if hasattr(_driver, "get_screenshot_as_png"):
            with allure.step('添加失败截图...'):
                allure.attach(_driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)


@pytest.fixture(scope='session',autouse=True)
def driver():
    global _driver
    warnings.simplefilter('ignore', ResourceWarning)
    _driver = Browser.open_browser('chrome')
    yield _driver
    time.sleep(2)
    _driver.quit()