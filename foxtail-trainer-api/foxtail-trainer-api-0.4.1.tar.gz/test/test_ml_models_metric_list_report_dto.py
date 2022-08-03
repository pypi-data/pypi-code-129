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
from foxtail_trainer_api.models.ml_models_metric_list_report_dto import MLModelsMetricListReportDto  # noqa: E501
from foxtail_trainer_api.rest import ApiException

class TestMLModelsMetricListReportDto(unittest.TestCase):
    """MLModelsMetricListReportDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MLModelsMetricListReportDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = foxtail_trainer_api.models.ml_models_metric_list_report_dto.MLModelsMetricListReportDto()  # noqa: E501
        if include_optional :
            return MLModelsMetricListReportDto(
                count = 56, 
                ml_model_metric_reports = [
                    foxtail_trainer_api.models.ml_model_metric_report_dto.MLModelMetricReportDto(
                        model_id = '0', 
                        training_metrics = [
                            foxtail_trainer_api.models.metric_report_dto.MetricReportDto(
                                metric_type = 'MAE', 
                                value = 1.337, )
                            ], 
                        validation_metrics = [
                            foxtail_trainer_api.models.metric_report_dto.MetricReportDto(
                                value = 1.337, )
                            ], 
                        test_metrics = [
                            foxtail_trainer_api.models.metric_report_dto.MetricReportDto(
                                value = 1.337, )
                            ], )
                    ]
            )
        else :
            return MLModelsMetricListReportDto(
        )

    def testMLModelsMetricListReportDto(self):
        """Test MLModelsMetricListReportDto"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
