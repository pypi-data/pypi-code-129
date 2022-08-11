import requests
import json
#from uuid import uuid4
import random, string

from ..response import ok, error


def _format(response):
    response['payment_id'] = response['site_transaction_id']
    response['amount'] = response['amount'] / 100
    response['date_created'] = response['date']
    response['status_detail'] = response['status']
    if response['status'] == 'accredited':
        response['status'] = 'approved'
        response['status_detail'] = 'accredited'
    elif response['status'] == 'approved':
        response['status_detail'] = 'not_accredited'

    return response


class Payment:
    def __init__(self, url, private_key: str, public_key: str):
        self.url = url
        self.private_key = private_key
        self.public_key = public_key
        self.headers = {
            'apikey': self.private_key,
            'Content-Type': 'application/json',
            'Cache-Control': 'no-cache'
        }

    def create(self, payment_data: dict):
        site_transaction_id = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        body = {
            'customer': {
                'id': payment_data['payer']['decidir_id'],
                'email': payment_data['payer']['email']
            },
            'site_transaction_id': site_transaction_id,#str(uuid4())
            'token': payment_data['token'],
            'payment_method_id': 1,    # Peso Argentino
            'bin': payment_data['bin'],    # primeros 6 digitos de la tarjeta
            # se multiplica por 100; no acepta decimales.
            'amount': round(payment_data['transaction_amount'], 2) * 100,
            'currency': 'ARS',
            'installments': 1,
            'payment_type': 'single',
            'establishment_name': '-',  # opcional
            'sub_payments': []
        }
        additional_information = [
            'installments',
            'establishment_name',
            'site_id',
            'sub_payments',
            'payment_type',
            'site_transaction_id'
        ]
        for item in additional_information:
            if item in payment_data.keys():
                body[item] = payment_data[item]

        r = requests.post(self.url + '/payments', headers=self.headers, data=json.dumps(body))
        response = r.json()
        response['processor'] = 'decidir'
        if r.status_code < 400:
            return ok(_format(response))
        return error(response)

    def get(self, payment_id: str):
        # r = requests.get(self.url + '/payments/{}'.format(payment_id), headers=self.headers)
        # return ok(_format(r.json()))
        filters = {'siteOperationId':payment_id}
        r = requests.get(self.url + '/payments', params=filters, headers=self.headers)
        list_results = r.json()['response']['results']
        if len(list_results) == 1:
            return _format(list_results[0])
        else:
            return error('error_pago_no_encontrado')
    def search(self, filters: dict) -> dict:
        # El filter puede ser:
        # offset
        # pageSize
        # siteOperationId
        # merchantId
        # dateFrom
        # dateTo
        # site
        r = requests.get(self.url + '/payments', params=filters, headers=self.headers)
        response = r.json()
        response['results'] = [_format(r) for r in response['results']]
        return ok(response)

    def get_payment_methods(self):
        r = requests.get(self.url + '/payment-methods/1',headers=self.headers)
        return r.json()