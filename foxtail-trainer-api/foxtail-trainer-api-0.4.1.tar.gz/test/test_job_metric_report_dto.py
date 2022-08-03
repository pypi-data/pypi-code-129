# coding: utf-8

"""
    Foxtail Trainer

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import foxtail_trainer_api
from foxtail_trainer_api.models.job_metric_report_dto import JobMetricReportDto  # noqa: E501
from foxtail_trainer_api.rest import ApiException

class TestJobMetricReportDto(unittest.TestCase):
    """JobMetricReportDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JobMetricReportDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = foxtail_trainer_api.models.job_metric_report_dto.JobMetricReportDto()  # noqa: E501
        if include_optional :
            return JobMetricReportDto(
                problem_type = 'Regression', 
                training_aggregated_metrics = [
                    foxtail_trainer_api.models.aggregated_metric_report_dto.AggregatedMetricReportDto(
                        models_count = 56, 
                        metric_type = 'MAE', 
                        average_value = 1.337, 
                        standard_deviation_value = 1.337, 
                        minimim_value = 1.337, 
                        maximum_value = 1.337, )
                    ], 
                validation_aggregated_metrics = [
                    foxtail_trainer_api.models.aggregated_metric_report_dto.AggregatedMetricReportDto(
                        models_count = 56, 
                        metric_type = 'MAE', 
                        average_value = 1.337, 
                        standard_deviation_value = 1.337, 
                        minimim_value = 1.337, 
                        maximum_value = 1.337, )
                    ], 
                test_aggregated_metrics = [
                    foxtail_trainer_api.models.aggregated_metric_report_dto.AggregatedMetricReportDto(
                        models_count = 56, 
                        metric_type = 'MAE', 
                        average_value = 1.337, 
                        standard_deviation_value = 1.337, 
                        minimim_value = 1.337, 
                        maximum_value = 1.337, )
                    ]
            )
        else :
            return JobMetricReportDto(
        )

    def testJobMetricReportDto(self):
        """Test JobMetricReportDto"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
