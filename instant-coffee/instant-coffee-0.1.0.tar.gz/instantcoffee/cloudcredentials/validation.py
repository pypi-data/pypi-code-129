"""
Validator of cloud credentials / cloud accounts

Searches integrated cloud accounts or alternatively checks credentials
"""
import datetime
import json

from abc import ABC, abstractmethod
from time import sleep

from instantcoffee.kaffeeservice import consts
from instantcoffee.kaffeeservice.api import Api
from instantcoffee.kaffeeservice.exceptions import ValidationException


class InvalidParamValue(Exception):
    """
    Exception to handle invalid values in dropdown parameters, etc.
    """

    def __init__(self, param_id: str, value: str):
        super().__init__('Invalid value {} for param {}'.format(value, param_id))

class Validator(ABC):
    """
    The credential validator validates the AWS / Azure credentials.

    Parameters:
    - req: the Connect request
    - kaffeeservice: the wrapper for the kaffeeservice microservice.
    - logger: The logger for the request

    It expects the following Connect parameters to be defined in the product:
    - 
    - CONNECT_PARAM_IMCO_CUSTOMER_ID
    - In case of "integrated" mode: CONNECT_PARAM_CREDENTIALS_SOURCE
      - ""/CONNECT_PARAM_CREDENTIALS_SOURCE_INTEGRATED: find integrated subscription
      - CONNECT_PARAM_CREDENTIALS_SOURCE_INTEGRATED: enter credentials manually
    """
    def __init__(self, req, kaffeeservice, logger):
        self._req= req
        self._kaffeeservice: Api = kaffeeservice
        self._logger= logger

    @abstractmethod
    def extract_credentials(self):
        """
        Extract cloud provider specific credentials from asset parameters
        """
        raise NotImplementedError # pragma: no cover

    @abstractmethod
    def mark_credentials_invalid(self, param_ids, logger, msg=None):
        """
        Mark cloud-provider specific credential parameters as invalid
        """
        raise NotImplementedError # pragma: no cover

    @abstractmethod
    def delete_secret_keys(self, param_ids: set):
        """
        Delete the cloud-provider specific secret key parameter
        """
        raise NotImplementedError # pragma: no cover

    @staticmethod
    @abstractmethod
    def cloud_provider_name() -> str:
        """
        Return the cloud provider name
        """
        raise NotImplementedError # pragma: no cover

    def validate(self, integrated: bool = True, inquiring: bool = True,
            timeout: datetime.datetime = None) -> set:
        """
        Validate cloud credentials in request

        Precondition: value errors have been cleared beforehand!

        Updates the parameter values or value errors inline.

        Returns a set of parameter ids (in Connect terminology: param names) that need to be updated
        """

        if not timeout:
            timeout = datetime.datetime.now()+datetime.timedelta(seconds=20)
        self._logger.info(f'Validate credentials - Timeout: {timeout}')
        asset = self._req.asset
        param_ids = set()

        customer_id = asset.get_param_value(consts.IMCO_CUSTOMER_ID)
        self._logger.debug(f'customer_id: {customer_id}')
        if not customer_id:
            self._logger.info('Create customer')
            customer = asset.tiers.customer
            value = self._kaffeeservice.create_customer(
                asset.connection.hub.id, asset.marketplace.id, customer.id, customer.external_id, customer.name)
            asset.update_parameter(consts.IMCO_CUSTOMER_ID, value)
            param_ids.add(consts.IMCO_CUSTOMER_ID)

        params = []
        cloud_account = asset.get_param_value(consts.DEPLOY_CLOUD_ACCOUNT)
        if cloud_account:
            # We assume that cloud provider did not change (currently guaranteed by Connect)
            self._logger.info(f'Validate: Cloud account already set to {cloud_account} - \
                nothing to do')
        elif integrated:
            self._logger.info('Try to get integrated subscription')
            credentials_source = asset.get_param_value(consts.CONNECT_PARAM_CREDENTIALS_SOURCE)
            self._logger.debug(f'credentials_source value: {credentials_source}')
            if not credentials_source or credentials_source == consts.CONNECT_PARAM_CREDENTIALS_SOURCE_INTEGRATED:
                self._find_integrated_account(param_ids, timeout=timeout)
            elif credentials_source == consts.CONNECT_PARAM_CREDENTIALS_SOURCE_MANUAL:
                params = self._validate_credentials(param_ids, inquiring=inquiring)
            else:
                raise InvalidParamValue(consts.CONNECT_PARAM_CREDENTIALS_SOURCE, credentials_source)
        else:
            self._logger.info('Standalone mode: Validate credentials')
            # Note: Don't allow cloud desk to get involved
            params = self._validate_credentials(param_ids, inquiring=inquiring)

        return param_ids, params

    def _find_integrated_account(self, param_ids: set, timeout: datetime.datetime):
        """
        Find integrated accounts.

        - If no integrated account found, or discovery timed out, will inquire credential_source parameter
        - If one integrated account found, will set this account as "cloud account param" and add id to param_ids
        - If more than one integrated account found, will set value error for cloud account param,
          setting value to first, and adding id to param_ids.
        """
        asset = self._req.asset
        customer_id = asset.get_param_value(consts.IMCO_CUSTOMER_ID)
        hub_id = asset.connection.hub.id
        mp_id = asset.marketplace.id
        cloud_provider = self.cloud_provider_name()
        self._kaffeeservice.discover_integrated_accounts(hub_id, mp_id, customer_id, cloud_provider)
        result = {'finished': False}
        self._logger.info(f'Seconds remaining: {(timeout - datetime.datetime.now()).seconds}')
        while not result.get('finished') and datetime.datetime.now() + datetime.timedelta(seconds=3) < timeout:
            sleep(3)
            result = self._kaffeeservice.list_integrated_accounts(hub_id, mp_id, customer_id, cloud_provider)
            self._logger.debug(f'result = {result}')
            self._logger.info(f'Seconds remaining: {(timeout - datetime.datetime.now()).seconds}')

        credentials_source = asset.get_param_value(consts.CONNECT_PARAM_CREDENTIALS_SOURCE)
        if result.get('finished'):
            cloud_accounts = result.get('cloud_accounts')
            if cloud_accounts:
                value_error = ''
                if len(cloud_accounts) > 1:
                    value_error = 'Please choose between {}'.format(', '.join(cloud_accounts))
                asset.update_parameter(consts.DEPLOY_CLOUD_ACCOUNT, cloud_accounts[0], value_error)
                param_ids.add(consts.DEPLOY_CLOUD_ACCOUNT)
            else:
                self._logger.info('Integrated cloud account not found')
                value_error = 'No {} subscription found'.format(cloud_provider)
                asset.update_parameter(consts.CONNECT_PARAM_CREDENTIALS_SOURCE, credentials_source, value_error)
                param_ids.add(consts.CONNECT_PARAM_CREDENTIALS_SOURCE)
        else:
            self._logger.info('Integrated cloud account discovery timed out')
            value_error = 'Discovery of {} subscription timed out'.format(cloud_provider)
            asset.update_parameter(consts.CONNECT_PARAM_CREDENTIALS_SOURCE, credentials_source, value_error)
            param_ids.add(consts.CONNECT_PARAM_CREDENTIALS_SOURCE)

    def _validate_credentials(self, param_ids: set, inquiring: bool):
        """
        Check if credentials have been entered manually, and validate them.

        If credentials have been entered and are valid, create cloud account,
        update the parameter and delete secret key.

        Otherwise, but only when inquiring (i.e. not in draft validation),
        mark credentials as missing or invalid (see CSO-1252).
        """
        self._logger.info('Get credentials from Connect params')
        cred_id, credentials = self.extract_credentials()
        self._logger.debug(f'cred_id: {cred_id}, credentials: {credentials}')
        if cred_id == "":
            self._logger.info('Credentials not given yet')
            # In draft validation, do not mark them as invalid. Don't trust CBC in handling credentials
            self._logger.debug(f'inquiring={inquiring}')
            if inquiring:
                return self.mark_credentials_invalid(param_ids, self._logger)
            return

        asset = self._req.asset
        customer_id = asset.get_param_value(consts.IMCO_CUSTOMER_ID)
        hub_id = asset.connection.hub.id
        mp_id = asset.marketplace.id
        try:
            self._logger.info('Try to create cloud account')
            cloud_account = self._kaffeeservice.create_cloud_account(
                hub_id, mp_id, customer_id, self.cloud_provider_name(), cred_id, credentials
            )
        except ValidationException as ex:
            self._logger.info('Credentials are invalid')
            # In draft validation, do not mark them as invalid. Don't trust CBC in handling credentials
            # In theory, we should not enter here during draft validation, anyway,
            # if the Connect param is well-defined as hidden
            if inquiring:
                data = json.loads(ex.body)
                msg = data.get('error')
                return self.mark_credentials_invalid(param_ids, self._logger, msg)
            return

        self._logger.info('Update deploy_cloud_account parameter')
        asset.update_parameter(consts.DEPLOY_CLOUD_ACCOUNT, cloud_account)
        param_ids.add(consts.DEPLOY_CLOUD_ACCOUNT)

        self._logger.info('Delete secret param')
        self.delete_secret_keys(param_ids)
