class ModernTreasuryException(Exception):
    def __init__(self, status_code, reason, url, json):
        Exception.__init__(self)
        self.reason = reason
        self.status_code = status_code
        self.url = url
        self.json = json
