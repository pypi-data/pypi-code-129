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
from foxtail_trainer_api.models.ml_models_guids_list_dto import MLModelsGuidsListDto  # noqa: E501
from foxtail_trainer_api.rest import ApiException

class TestMLModelsGuidsListDto(unittest.TestCase):
    """MLModelsGuidsListDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MLModelsGuidsListDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = foxtail_trainer_api.models.ml_models_guids_list_dto.MLModelsGuidsListDto()  # noqa: E501
        if include_optional :
            return MLModelsGuidsListDto(
                count = 56, 
                guids = [
                    '0'
                    ]
            )
        else :
            return MLModelsGuidsListDto(
        )

    def testMLModelsGuidsListDto(self):
        """Test MLModelsGuidsListDto"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
