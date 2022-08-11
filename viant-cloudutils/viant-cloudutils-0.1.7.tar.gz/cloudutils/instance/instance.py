#!/usr/bin/env python

import requests
import logging


class Instance:

    @staticmethod
    def get_cloud_provider(**kwargs):
        provider = ""
        if "computeMetadata/" in requests.get("http://169.254.169.254/").text:
            provider = "gcp"
        else:
            provider = "aws"
        return provider
