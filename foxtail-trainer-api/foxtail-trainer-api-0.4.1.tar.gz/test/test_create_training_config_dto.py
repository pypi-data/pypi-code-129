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
from foxtail_trainer_api.models.create_training_config_dto import CreateTrainingConfigDto  # noqa: E501
from foxtail_trainer_api.rest import ApiException

class TestCreateTrainingConfigDto(unittest.TestCase):
    """CreateTrainingConfigDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateTrainingConfigDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = foxtail_trainer_api.models.create_training_config_dto.CreateTrainingConfigDto()  # noqa: E501
        if include_optional :
            return CreateTrainingConfigDto(
                data_sets_sizes = foxtail_trainer_api.models.create_data_sets_sizes_dto.CreateDataSetsSizesDto(
                    realative_size = True, 
                    training_set_apsolute_size = 56, 
                    training_set_realtive_size = 1.337, 
                    validation_set_apsolute_size = 56, 
                    validation_set_realtive_size = 1.337, 
                    test_set_apsolute_size = 56, 
                    test_set_realtive_size = 1.337, ), 
                features = [
                    '0'
                    ], 
                targets = [
                    '0'
                    ], 
                problem_type = 'Regression', 
                model_type = 'Xgboost', 
                model_hyperparameters = [
                    foxtail_trainer_api.models.create_model_hyperparameter_dto.CreateModelHyperparameterDto(
                        name = '0', 
                        value = '0', )
                    ]
            )
        else :
            return CreateTrainingConfigDto(
        )

    def testCreateTrainingConfigDto(self):
        """Test CreateTrainingConfigDto"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
