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
from foxtail_trainer_api.models.job_training_config_dto import JobTrainingConfigDto  # noqa: E501
from foxtail_trainer_api.rest import ApiException

class TestJobTrainingConfigDto(unittest.TestCase):
    """JobTrainingConfigDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JobTrainingConfigDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = foxtail_trainer_api.models.job_training_config_dto.JobTrainingConfigDto()  # noqa: E501
        if include_optional :
            return JobTrainingConfigDto(
                data_sets_sizes = foxtail_trainer_api.models.update_data_sets_sizes_dto.UpdateDataSetsSizesDto(
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
                add_or_update_model_hyperparameter_in_job = [
                    foxtail_trainer_api.models.add_or_update_model_hyperparameter_in_job.AddOrUpdateModelHyperparameterInJob(
                        name = '0', 
                        value = '0', )
                    ], 
                remove_model_hyperparameters_from_job = [
                    '0'
                    ]
            )
        else :
            return JobTrainingConfigDto(
        )

    def testJobTrainingConfigDto(self):
        """Test JobTrainingConfigDto"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
