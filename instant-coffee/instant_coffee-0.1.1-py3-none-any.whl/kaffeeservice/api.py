"""
The kaffeeservice API interface
"""
from datetime import datetime, timedelta
from typing import Tuple
from urllib.parse import quote, urlencode

import io
import secrets
import jwt

from requests import Session
from instantcoffee.kaffeeservice.exceptions import service_exception

class Api:
    """
    Kaffeeservice API
    """

    def __init__(self, vendor_id, logger, deployer_audience, deployer_endpoint, 
        deployer_jwt_key, ca_file=None):
        self._logger = logger
        self._logger.info('Initializing kaffeeservice API')
        self._vendor_id = vendor_id
        self._endpoint = deployer_endpoint.rstrip('/')
        self._audience = deployer_audience
        self._pem_key = deployer_jwt_key
        self._session = Session()
        if ca_file:
            self._session.verify = ca_file

    def set_headers(self) -> dict:
        """
        Set Authorization and Content-Type header
        """
        jwt_payload = {
            'iss': self._vendor_id,
            'aud': self._audience,
            'nbf': datetime.utcnow() - timedelta(seconds=10),
            'exp': datetime.utcnow() + timedelta(seconds=20),
            'jti': secrets.token_urlsafe(20)
        }
        token = jwt.encode(jwt_payload, self._pem_key, algorithm='PS512')
        return {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(token)
        }


    def get(self, path: str, query: dict = None):
        """
        Sends a GET request

        :param path: relative path for request

        :return: json-decoded content of response

        :raises service_exception
        """
        if query:
            qstr = urlencode(query)
            path = '{}?{}'.format(path, qstr)
        self._logger.debug('GET {}{}'.format(self._endpoint, path))
        headers = self.set_headers()
        self._logger.debug(f'headers={headers}')
        response = self._session.get(self._endpoint + path, headers=headers)
        if not response:
            raise service_exception(response.status_code, response.content)
        self._logger.debug(f'response: {response.json()}')
        return response.json()

    def put(self, path: str, body):
        """
        Sends a PUT request

        :param path: path for the request
        :param body: arguments for the request

        :return: json-decoded content of response

        :raises service_exception
        """
        self._logger.debug('PUT {}{} with body {}'.format(self._endpoint, path, body))
        response = self._session.put(self._endpoint + path, json=body, headers=self.set_headers())
        if not response:
            raise service_exception(response.status_code, response.content)
        if response.content:
            self._logger.debug(f'response: {response.json()}')
            return response.json()
        self._logger.debug('No response')

    def post(self, path: str, body):
        """
        Sends a POST request

        :param path: path for the request
        :param body: arguments for the request

        :return: json-decoded content of response

        :raises service_exception
        """
        self._logger.debug('POST {}{} with body {}'.format(self._endpoint, path, body))
        headers = self.set_headers()
        self._logger.debug(f'headers={headers}')
        response = self._session.post(self._endpoint + path, json=body, headers=headers)
        if not response:
            raise service_exception(response.status_code, response.content)
        if response.content:
            self._logger.debug(f'response: {response.json()}')
            return response.json()
        self._logger.debug('No response')
        
    def delete(self, path: str) -> bool:
        """
        Sends a DELETE request

        :param path: path for the request

        Returns if delete was finished (False: only Accepted)

        :raises service_exception
        """
        self._logger.debug('DELETE {}{}'.format(self._endpoint, path))
        response = self._session.delete(self._endpoint + path, headers=self.set_headers())
        if not response:
            raise service_exception(response.status_code, response.content)
        if response.status_code == 202:
            return False
        return True

    def get_cat(self, hub_id: str, mp_id: str, name: str, version: str) -> str:
        """
        Calls ExistsCAT on the kaffeeservice.

        Returns cat_id

        Note: Do not use names and versions containing slashes. While we could easily encode them,
        kaffeeservice is currently not able to decode them as the decoding leads to arbitrary results
        """
        path = '/hubs/{}/marketplaces/{}/cats/{}/versions/{}'\
            .format(hub_id, mp_id, quote(name), quote(version))
        result = self.get(path)
        return result.get('id')

    def upload_cat(self, hub_id: str, mp_id: str, name: str, version: str, file: io.IOBase) -> str:
        """
        Upload CAT

        Data should be file-like object (but can also be bytes)
        
        :raises service_exception
        """
        path = '/hubs/{}/marketplaces/{}/cats/{}/versions/{}'\
            .format(hub_id, mp_id, quote(name), quote(version))
        self._logger.debug('POST {}{}'.format(self._endpoint, path))
        response = self._session.post(self._endpoint + path, headers=self.set_headers(), data=file)
        if not response:
            raise service_exception(response.status_code, response.content)
        self._logger.debug(response.json())
        result = response.json()
        return result.get('id')

    def create_customer(self, hub_id: str, mp_id: str, connect_id: str, connect_external_id: str, name: str) -> str:
        """
        Create customer, if it does not exist yet.

        Otherwise, get existing customer.

        Returns IMCO customer ID
        """
        path = '/hubs/{}/marketplaces/{}/customers'.format(hub_id, mp_id)
        body = {
            'id': connect_id,
            'external_id': connect_external_id,
            'name': name
        }
        return self.post(path, body).get('customer_id')

    def discover_integrated_accounts(self, hub_id: str, mp_id: str, customer_id: str, cloud_provider: str):
        """
        Launch discovery of integrated cloud accounts
        """
        path = '/hubs/{}/marketplaces/{}/customers/{}/integrated-accounts/discover'.format(hub_id, mp_id, customer_id)
        body = {'cloud_provider': cloud_provider}
        self.put(path, body)

    def list_integrated_accounts(self, hub_id: str, mp_id: str, customer_id: str, cloud_provider: str) -> dict:
        """
        Lists integrated accounts, if discovery is finished

        Returns a dict with finished: bool, and optionally accounts: List[str]
        Note: Failed discovery is handled as finished discovery
        """
        query = {'cloud_provider': cloud_provider}
        path = '/hubs/{}/marketplaces/{}/customers/{}/integrated-accounts'.\
                format(hub_id, mp_id, customer_id)
        return self.get(path, query)

    def create_cloud_account(self,
            hub_id: str, mp_id: str, customer_id: str, cloud_provider: str, credential_id: str, credentials: dict
        ) -> str:
        """
        Create a new stand-alone cloud account
        Reuse existing, if cloud account with same credential_id exists

        Returns name of cloud account
        """
        path = '/hubs/{}/marketplaces/{}/customers/{}/standalone-accounts'.format(hub_id, mp_id, customer_id)
        body = {
            'cloud_provider': cloud_provider,
            'credential_id': credential_id,
            'credentials': credentials
        }
        return self.post(path, body).get('cloud_account')

    def create_deployment(self,
            hub_id: str, mp_id: str, customer_id: str, label: str, vendor_cat_id: str, inputs: dict
        ) -> Tuple[str, str]:
        """
        Create a deployment with label

        Returns dict with cat_id (on customer level) and task_id

        If label already exists, we get a ValidationError with errors->name error list
        """
        path = '/hubs/{}/marketplaces/{}/customers/{}/deployments/{}'\
            .format(hub_id, mp_id, customer_id, quote(label))
        body = {
            'cat_id': vendor_cat_id,
            'inputs': inputs
        }

        result = self.post(path, body)
        return result.get('cat_id'), result.get('task_id')

    def get_deployment_task(self,
        hub_id: str, mp_id: str, customer_id: str, cat_id: str, task_id:str
    ) -> Tuple[bool, dict, str]:
        """
        Get deployment task

        Returns a dict with:
            - finished: bool (independently if success or failure)
            - outputs: dict (optional - successfully finished)
            - error_message: str (optional - failed)
        """
        path = '/hubs/{}/marketplaces/{}/customers/{}/cats/{}/tasks/{}'.\
                format(hub_id, mp_id, customer_id, cat_id, task_id)
        result = self.get(path)
        return result.get('finished'), result.get('outputs'), result.get('error_message')

    def undeploy(self, hub_id: str, mp_id: str, customer_id: str, label: str) -> bool:
        """
        Delete a deployment

        Returns if finished

        If label already exists, we get a ValidationError with errors->name error list
        """
        path = '/hubs/{}/marketplaces/{}/customers/{}/deployments/{}'\
            .format(hub_id, mp_id, customer_id, quote(label))

        return self.delete(path)
