class AccountDetailsResponse:
    def __init__(self, json):
        self.json = json

    @property
    def id(self):
        return self.json.get('id')

    @property
    def account_number(self):
        return self.json.get('account_number')

    @property
    def account_number_type(self):
        return self.json.get('account_number')

    @property
    def live_mode(self):
        return self.json.get('live_mode')
