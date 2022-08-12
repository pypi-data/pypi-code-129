# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['authapi',
 'authapi.providers',
 'authapi.providers.facebook',
 'authapi.providers.google',
 'authapi.providers.microsoft']

package_data = \
{'': ['*'], 'authapi': ['templates/*']}

install_requires = \
['Flask>=2.1.2,<3.0.0',
 'cffi>=1.15.0,<2.0.0',
 'pyOpenSSL>=22.0.0,<23.0.0',
 'pydantic>=1.9.1,<2.0.0',
 'requests-oauthlib>=1.3.1,<2.0.0']

setup_kwargs = {
    'name': 'authapi',
    'version': '0.1.14',
    'description': 'OAuth2 Code Grant Authentication API',
    'long_description': '# AuthAPI\n\nA Simple Python API for Authenticated Operations.\n\n![landing_img](https://raw.githubusercontent.com/manucalop/authapi/main/docs/img/landing.png)\n\n## Quickstart:\n\nLet\'s assume you want to interact with Google Ads API.\n\n1. Create `my_secret.json` with the following information:\n\n```json\n{\n    "client_id": "",\n    "client_secret": "",\n    "authorize_url": "",\n    "access_token_url": "",\n    "scopes": []\n}\n\n```\n\n2. Create a `main.py` script and paste the following content.\n\n```python\nfrom authapi import AuthAPI, AuthData\n\nclass JsonSecret:\n    def __init__(self, path: str):\n        self.path = path\n\n    def pull(self) -> dict:\n        with open(self.path, "r") as f:\n            return json.load(f)\n\n    def push(self, payload: dict) -> None:\n        with open(self.path, "w") as f:\n            json.dump(payload, f)\n\napp_secret = JsonSecret("my_secret.json")\napp_token = JsonSecret("my_token.json")\n\nauth_data = AuthData(**app_secret.pull())\n\napp = AuthAPI(\n    name="Auth API: My Auth API",\n    auth_data=auth_data,\n    token_secret=app_token,\n)\n\napp.debug = True\n\n\n@app.route("/run", methods=["GET", "POST"])\ndef run():\n    token = app.get_token()\n    # Do your stuff here\n    return "Done!"\n\n\nif __name__ == "__main__":\n    app.run(ssl_context="adhoc")\n```\n\n3. Run `python main.py` and visit [https://127.0.0.1:5000/](https://127.0.0.1:5000/) to start the authentication process.\n',
    'author': 'Manuel Castillo-Lopez',
    'author_email': 'manucalop@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/manucalop/authapi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
