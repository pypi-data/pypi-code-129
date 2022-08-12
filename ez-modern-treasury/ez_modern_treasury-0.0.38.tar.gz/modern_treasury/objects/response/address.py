class AddressResponse:
    def __init__(self, json):
        self.json = json

    @property
    def id(self):
        return self.json.get('id')

    @property
    def line1(self):
        return self.json.get('line1')

    @property
    def line2(self):
        return self.json.get('line2')

    @property
    def locality(self):
        return self.json.get('locality')

    @property
    def region(self):
        return self.json.get('region')

    @property
    def postal_code(self):
        return self.json.get('postal_code')

    @property
    def country(self):
        return self.json.get('country')
