from .address import AddressResponse


class RoutingDetailsResponse:
    def __init__(self, json):
        self.json = json

    @property
    def id(self):
        return self.json.get('id')

    @property
    def bank_name(self):
        return self.json.get('bank_name')

    @property
    def routing_number(self):
        return self.json.get('routing_number')

    @property
    def routing_number_type(self):
        return self.json.get('routing_number_type')

    @property
    def bank_address(self):
        result = self.json.get('bank_address')
        if result:
            return AddressResponse(result)
        return None
