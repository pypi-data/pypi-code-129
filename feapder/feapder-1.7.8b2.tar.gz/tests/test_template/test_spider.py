# -*- coding: utf-8 -*-
"""
Created on 2022-08-03 17:35:15
---------
@summary:
---------
@author: Boris
"""

import feapder
from feapder import ArgumentParser


class TestSpider(feapder.BatchSpider):
    # 自定义数据库，若项目中有setting.py文件，此自定义可删除
    __custom_setting__ = dict(
        REDISDB_IP_PORTS="localhost:6379",
        REDISDB_USER_PASS="",
        REDISDB_DB=0,
        MYSQL_IP="localhost",
        MYSQL_PORT=3306,
        MYSQL_DB="",
        MYSQL_USER_NAME="",
        MYSQL_USER_PASS="",
    )

    def start_requests(self, task):
        yield feapder.Request("https://spidertools.cn")

    def parse(self, request, response):
        # 提取网站title
        print(response.xpath("//title/text()").extract_first())
        # 提取网站描述
        print(response.xpath("//meta[@name='description']/@content").extract_first())
        print("网站地址: ", response.url)


if __name__ == "__main__":
    spider = TestSpider(
        redis_key="xxx:xxxx",  # 分布式爬虫调度信息存储位置
        task_table="",  # mysql中的任务表
        task_keys=["id", "xxx"],  # 需要获取任务表里的字段名，可添加多个
        task_state="state",  # mysql中任务状态字段
        batch_record_table="xxx_batch_record",  # mysql中的批次记录表
        batch_name="xxx(周全)",  # 批次名字
        batch_interval=7,  # 批次周期 天为单位 若为小时 可写 1 / 24
    )

    parser = ArgumentParser(description="TestSpider爬虫")

    parser.add_argument(
        "--start_master",
        action="store_true",
        help="添加任务",
        function=spider.start_monitor_task,
    )
    parser.add_argument(
        "--start_worker", action="store_true", help="启动爬虫", function=spider.start
    )

    parser.start()

    # 直接启动
    # spider.start()  # 启动爬虫
    # spider.start_monitor_task() # 添加任务

    # 通过命令行启动
    # python test_spider.py --start_master  # 添加任务
    # python test_spider.py --start_worker  # 启动爬虫
