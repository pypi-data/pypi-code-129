from typing import List

from .account import AccountResponse
from .routing_details import RoutingDetailsResponse


class CounterPartyResponse:
    def __init__(self, json):
        self.json = json

    @property
    def id(self) -> str:
        return self.json.get("id")

    @property
    def name(self) -> str:
        return self.json.get("name")

    @property
    def accounts(self) -> List[AccountResponse]:
        account_details = self.json.get("accounts")
        return [AccountResponse(account_detail) for account_detail in account_details]

    @property
    def routing_details(self) -> List[RoutingDetailsResponse]:
        routing_details = self.json.get("routing_details")
        return [RoutingDetailsResponse(routing_detail) for routing_detail in routing_details]

    @property
    def metadata(self) -> str:
        return self.json.get("metadata")

