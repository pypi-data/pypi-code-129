# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['intersight_auth']

package_data = \
{'': ['*']}

install_requires = \
['cryptography>=37.0.2,<38.0.0', 'requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'intersight-auth',
    'version': '0.2.4',
    'description': 'Intersight Authentication helper for requests',
    'long_description': '[![CI Tests](https://github.com/cgascoig/intersight-auth/actions/workflows/ci.yml/badge.svg)](https://github.com/cgascoig/intersight-auth/actions/workflows/ci.yml)\n# intersight-auth\n\nThis module provides an authentication helper for requests to make it easy to make [Intersight API](https://intersight.com/apidocs/introduction/overview/) calls using [requests](https://requests.readthedocs.io/en/latest/). \n\n## Features\n- Supports both v2 and v3 keys\n- Keys can be supplied as strings or path to a PEM file\n\n## Install\n\n```\npip install intersight-auth\n```\n\n## Example using a file for the secret key\n\n``` Python\nimport sys\n\nfrom intersight_auth import IntersightAuth\nfrom requests import Session\n\nsession = Session()\nsession.auth = IntersightAuth("XYZ/XYZ/XYZ", "key.pem")\n\nresponse = session.get("https://intersight.com/api/v1/ntp/Policies")\n\nif not response.ok:\n    print(f"Error: {response.status_code} {response.reason}")\n    sys.exit(1)\n\nfor policy in response.json()["Results"]:\n    print(f"{policy[\'Name\']}")\n```\n\n## Example using a multiline (a.k.a. heredoc) string for the secret key\n\nThe secret key must still be in PEM format even if it\'s a string instead of a file.\n\n``` Python\nmy_secret_key=\'\'\'\n-----BEGIN RSA PRIVATE KEY-----\nABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890/abcdefghizjklmnopqrstuvwxy\nABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890/abcdefghizjklmnopqrstuvwxy\nABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890/abcdefghizjklmnopqrstuvwxy\nABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890/abcdefghizjklmnopqrstuvwxy\nABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890/abcdefghizjklmnopqrstuvwxy\nABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890/abcdefghizjklmnopqrstuvwxy\nABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890/abcdefghizjklmnopqrstuvwxy\nABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890/abcdefghizjklmnopqrstuvwxy\nABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890/abcdefghizjklmnopqrstuvwxy\nABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890/abcdefghizjklmnopqrstuvwxy\nABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890/abcdefghizjklmnopqrstuvwxy\nABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890/abcdefghizjklmnopqrstuvwxy\nABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890/abcdefghizjklmnopqrstuvwxy\nABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890/abcdefghizjklmnopqrstuvwxy\nABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890/abcdefghizjklmnopqrstuvwxy\nABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890/abcdefghizjklmnopqrstuvwxy\nABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890/abcdefghizjklmnopqrstuvwxy\nABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890/abcdefghizjklmnopqrstuvwxy\nABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890/abcdefghizjklmnopqrstuvwxy\nABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890/abcdefghizjklmnopqrstuvwxy\nABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890/abcdefghizjklmnopqrstuvwxy\nABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890/abcdefghizjklmnopqrstuvwxy\nABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890/abcdefghizjklmnopqrstuvwxy\nABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890/abcdefghizjklmnopqrstuvwxy\nABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890/abcdefghizjklmnopqrstuvwxy\nABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890/abcdefghizjkl=\n-----END RSA PRIVATE KEY-----\n\'\'\'\n\nsession = Session()\nsession.auth = IntersightAuth(\n    api_key_id="XYZ/XYZ/XYZ", \n    secret_key_string=my_secret_key\n    )\n\nresponse = session.get("https://intersight.com/api/v1/ntp/Policies")\n\nif not response.ok:\n    print(f"Error: {response.status_code} {response.reason}")\n    sys.exit(1)\n\nfor policy in response.json()["Results"]:\n    print(f"{policy[\'Name\']}")\n```\n\n## Example of PEM repair\n\nThe need to present the secret key in PEM format can be a challenge with some secret management approaches.  The PEM could be collapsed onto a single line, or the whitespace could otherwise be disturbed.  A function is provided to attempt to resolve these kinds of issues.\n\n``` Python\n\nfrom intersight_auth import IntersightAuth, repair_pem\n\n# This PEM has required the whitespace removed\nbroken_pem = "-----BEGIN EC PRIVATE KEY-----ABCDEFGHIJKLMNOPQRSTUVWXYZ012345678900abcdefghizjklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXYZ012345678900abcdefghizjklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXYZ012345678900abcdefghizjklmnopq-----END EC PRIVATE KEY-----"\n\nsession = Session()\nsession.auth = IntersightAuth(\n    api_key_id="XYZ/XYZ/XYZ", \n    secret_key_string=repair_pem(broken_pem)\n    )\n\n```',
    'author': 'Chris Gascoigne',
    'author_email': 'cgascoig@cisco.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/cgascoig/intersight-auth',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
