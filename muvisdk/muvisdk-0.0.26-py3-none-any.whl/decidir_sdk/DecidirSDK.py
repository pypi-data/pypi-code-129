from .Customer import Customer
from .Card import Card
from .CardToken import CardToken
from .Payment import Payment
from .Refund import Refund


class DecidirSDK:
    def __init__(self, merchant, merchant_cadena=None,site_id=None):
        if merchant_cadena:
            credentials = merchant_cadena['credentials']['decidir']
            self.payment_type = 'distributed'
        else:
            credentials = merchant['credentials']['decidir']
            self.payment_type = 'single'
        self.url = 'https://developers.decidir.com/api/v2'
        self.private_key = credentials['access_token']
        self.public_key = credentials['public_key']
        self.merchant_id = merchant['_id']
        self.merchant_name = merchant['name']
        self.site_id = site_id

    def customer(self):
        return Customer(self.url, self.private_key, self.public_key)
    
    def card(self):
        return Card(self.url, self.private_key, self.public_key)

    def card_token(self):
        return CardToken(self.url, self.private_key, self.public_key)

    def payment(self):
        return Payment(self.url, self.private_key, self.public_key, self.payment_type)

    def refund(self):
        return Refund(self.url, self.private_key, self.public_key)
