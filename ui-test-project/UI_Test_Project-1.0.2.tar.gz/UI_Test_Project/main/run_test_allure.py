# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : 小易
# @File : run_test_allure.py
# @Project : webuitestpythonProject
import os
import pytest
import threading
from UI_Test_Project.common.report import Report

project_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
report_dir = os.path.join(project_root, 'report')
result_dir = os.path.join(report_dir, 'allure_result')
allure_report = os.path.join(report_dir, 'allure_report')

report = Report()

tag = 'news'

def run_pytest():
    result_dir_list = os.listdir(result_dir)
    for f in result_dir_list:
        file_path = os.path.join(report_dir, f)
        if os.path.isfile(file_path):
            os.remove(file_path)

    pytest.main(['-v', '-s', '-m', f'{tag}', f'--alluredir={result_dir}'])

def general_report():
    cmd = "{} generate {} -o {} --clean".format(report.allure, result_dir, allure_report)
    print(os.popen(cmd).read())

if __name__ == "__main__":
    run = threading.Thread(target=run_pytest)
    gen = threading.Thread(target=general_report)
    run.start()
    run.join()
    gen.start()
    gen.join()