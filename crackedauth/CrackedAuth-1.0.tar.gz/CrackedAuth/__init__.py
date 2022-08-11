import requests
import uuid

class Cracked:
    auth_key = None

    def __init__(self, auth_key):
        self.auth_key = auth_key
        self.base_url = 'cracked.io/auth.php'
        self.endpoint_url = 'https://cracked.io/auth.php'
        self.version = '1.1'
        self.response = []
        self.data_response = []
        self.other_error = []

        source = {
            "a": "auth",
            "k": self.auth_key,
            "hwid": str(uuid.getnode())
        }

        request = requests.post(
            url = self.endpoint_url,
            data = source
        )
        text = request.text

        if '{"error":"invalid key"}' in text:
            return self.response.append('error')
        else:
            try:
                data = request.json()
                
                try:
                    account_name = data['username']
                    uid = data['uid']
                    posts = data['posts']
                    likes = data['likes']
                    groups = data['group']
                    
                    if groups == '':
                        groups = 'No groups'
                    else:
                        groups = groups
                except:
                    account_name = None
                    uid = None
                    posts = None
                    likes = None
                    groups = None
                    
                self.data_response.append(account_name)
                self.data_response.append(uid)
                self.data_response.append(posts)
                self.data_response.append(likes)
                self.data_response.append(groups)
                
                return self.response.append('succes')
            except:
                return self.other_error.append('Other error :/')