from typing import List

from .account_details import AccountDetailsResponse
from .routing_details import RoutingDetailsResponse


class AccountResponse:
    def __init__(self, json):
        self.json = json

    @property
    def id(self):
        return self.json.get('id')

    @property
    def name(self):
        return self.json.get('name')

    @property
    def account_details(self):
        account_details_list = []
        account_details = self.json.get('account_details')
        if account_details:
            account_details_list = [AccountDetailsResponse(details) for details in account_details]
        return account_details_list

    @property
    def routing_details(self) -> List[RoutingDetailsResponse]:
        routing_details_list = []
        routing_details = self.json.get('routing_details')
        if routing_details:
            routing_details_list = [RoutingDetailsResponse(details) for details in routing_details]
        return routing_details_list
