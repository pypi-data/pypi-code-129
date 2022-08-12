"""
AWS validator "interacts" with Connect asset parameters related to AWS
"""
from typing import Dict, Tuple
from instantcoffee.kaffeeservice import consts
from instantcoffee.cloudcredentials.validation import Validator


class AwsValidator(Validator):
    """
    Check AWS credentials

    It assumes the following additional parameters to be present in the request:
    - imco_aws_access_key_id
    - imco_aws_secret_access_key
    """
    @staticmethod
    def cloud_provider_name() -> str:
        return 'AWS'

    def __init__(self, req, kaffeeservice, logger, doc_link):
        self._doc_link = doc_link
        super().__init__(req, kaffeeservice, logger)

    def extract_credentials(self) -> Tuple[str, Dict[str, str]]:
        """
        Extracts the AWS credentials, expected to exist as Connect parameters prefixed by imco_aws_
        """
        asset = self._req.asset
        credentials = {}
        for cred_param_id in consts.AWS_CREDENTIAL_PARAMS:
            cred_id = cred_param_id[len('imco_aws_'):]
            param = asset.get_param_value(cred_param_id)
            credentials[cred_id] = param.strip()

        return credentials['access_key_id'], credentials

    def mark_credentials_invalid(self, param_ids: set, logger,
        message: str = 'To learn how to obtain AWS credentials, please visit the following URL'):
        """
        Marks the AWS credentials fields as invalid (with message and doc link)
        """
        params = []
        for cred_param_id in consts.AWS_CREDENTIAL_PARAMS:
            param_val = self._req.asset.get_param_value(cred_param_id)
            if cred_param_id == consts.AWS_SECRET_ACCESS_KEY_PARAM:
                param_val = ''
            logger.debug(f'updating value error for param {cred_param_id}')
            value_error = '{}: {}'.format(message, self._doc_link)
            param_ids.add(cred_param_id)
            param = self._req.asset.update_parameter(cred_param_id, param_val, value_error)
            logger.debug(f'param to update: {param}')
            params.append(param)
        return params

    def delete_secret_keys(self, param_ids: set):
        """
        Delete the secret key parameter value
        """
        param_ids.add(consts.AWS_SECRET_ACCESS_KEY_PARAM)
        self._req.asset.update_parameter(consts.AWS_ACCESS_KEY_PARAM, 'no longer needed')
