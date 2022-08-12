#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
               ..
              ( '`<
               )(
        ( ----'  '.
        (         ;
         (_______,' 
    ~^~^~^~^~^~^~^~^~^~^~
    Author: ThongNV
    Company: M O B I O
    Date Created: 5/25/22
"""
import os
import sys
from datetime import datetime
from os.path import exists

import requests

DATA_DIR = os.environ.get("APPLICATION_DATA_DIR")
SLACK_WEB_HOOK = os.environ.get("SLACK_URI_RESTART_POD")
POD_NAME = os.environ.get("HOSTNAME")


def get_topic_kafka(group_id):
    try:
        # Read file group data
        file_group_data = DATA_DIR + "/kafka-monitor-data" + "/{}.json".format(group_id)
        if exists(file_group_data):
            f = open(file_group_data)
            groups_data = f.read()
            if not groups_data:
                return 0
            if groups_data:
                groups_data = eval(groups_data)
            # Kiểm tra thời gian update file, nếu out date quá thì k áp dụng để restart
            m_time = groups_data.get("updated_time")
            # dt_m = datetime.fromtimestamp(m_time)
            duration = datetime.utcnow().timestamp() - m_time  # Số giây kể từ thời điểm update file
            # Nếu dữ liệu file data update quá 10 phút thì k kiểm tra nữa
            if duration > 600:
                return 0
        else:
            return 0

        # Read file config
        file_path = "/tmp/kafka-consumer-config.txt"
        if exists(file_path):
            f = open(file_path)
            consumer_config = f.read()
            if consumer_config:
                configs = consumer_config.split(":")
                if configs:
                    pod_config = configs[0]
                    if pod_config == POD_NAME:
                        consumer_id = configs[1]
                        members_id = groups_data.get("members_id")
                        if isinstance(members_id, list):
                            if consumer_id not in members_id:
                                return 1

        return 0
    except Exception:

        return 0


def warning_slack(group_id, pod_name):
    try:
        data_json = {
            "attachments": [
                {
                    "color": "#dc3907",
                    "pretext": "Consumer restart",
                    "title": "Pod name: {}".format(pod_name),
                    "author_name": "Group Name: {}".format(group_id),
                    "text": "Time: {}".format(datetime.utcnow())
                }
            ]
        }
        url = SLACK_WEB_HOOK
        if not url:
            url = "https://hooks.slack.com/services/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"
        requests.post(url, json=data_json)
    except Exception as ex:
        print("Error: ", ex)


if __name__ == '__main__':
    group_id = sys.argv[1] if len(sys.argv) > 1 else None
    check_status = get_topic_kafka(group_id)
    if check_status == 1:
        # Push slack restart pod
        warning_slack(group_id, POD_NAME)
        print("NotWorker")
    else:
        print("Alive")
