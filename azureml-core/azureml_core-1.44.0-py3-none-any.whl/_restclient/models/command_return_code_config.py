# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator 2.3.33.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CommandReturnCodeConfig(Model):
    """Configure how command return code is interpreted
    The return code success is determined by ReturnCode field
    Additional successful codes can be configured using SuccessfulReturnCodes
    field.

    :param return_code: Controls how command return code is interpreted.
     A failed return code means the run will fail due to user error
     Values can be provided as part of environment variable
     AZUREML_SUCCESSFUL_RETURN_CODE_CONDITION, too. Possible values include:
     'Zero', 'ZeroOrGreater'
    :type return_code: str or ~_restclient.models.SuccessfulCommandReturnCode
    :param successful_return_codes: Define additional return codes that are
     considered successful
     If ReturnCode = SuccessfulCommandReturnCode.Zero then
     SuccessfulReturnCodes can be used to specify other successful codes
     besides zero
     If ReturnCode = SuccessfulCommandReturnCode.ZeroOrGreater then
     SuccessfulReturnCodes can be used to specify which negative codes are
     successful
     Values can be provided as part of environment variable
     AZUREML_SUCCESSFUL_ADDITIONAL_RETURN_CODES, too
    :type successful_return_codes: list[int]
    """

    _attribute_map = {
        'return_code': {'key': 'returnCode', 'type': 'SuccessfulCommandReturnCode'},
        'successful_return_codes': {'key': 'successfulReturnCodes', 'type': '[int]'},
    }

    def __init__(self, return_code=None, successful_return_codes=None):
        super(CommandReturnCodeConfig, self).__init__()
        self.return_code = return_code
        self.successful_return_codes = successful_return_codes
