# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['web_database']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'web-database',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3',
}


setup(**setup_kwargs)
