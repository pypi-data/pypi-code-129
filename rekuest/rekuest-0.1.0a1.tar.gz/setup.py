# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rekuest']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'rekuest',
    'version': '0.1.0a1',
    'description': '',
    'long_description': None,
    'author': 'jhnnsrs',
    'author_email': 'jhnnsrs@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
