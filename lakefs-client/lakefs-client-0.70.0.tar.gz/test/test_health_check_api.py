"""
    lakeFS API

    lakeFS HTTP API  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: services@treeverse.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import lakefs_client
from lakefs_client.api.health_check_api import HealthCheckApi  # noqa: E501


class TestHealthCheckApi(unittest.TestCase):
    """HealthCheckApi unit test stubs"""

    def setUp(self):
        self.api = HealthCheckApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_health_check(self):
        """Test case for health_check

        """
        pass


if __name__ == '__main__':
    unittest.main()
