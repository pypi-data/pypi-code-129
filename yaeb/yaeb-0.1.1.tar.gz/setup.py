# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yaeb']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'yaeb',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Daniil Fedyaev',
    'author_email': 'wintercitizen@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
