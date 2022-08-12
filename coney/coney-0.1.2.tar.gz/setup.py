# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['coney']

package_data = \
{'': ['*']}

install_requires = \
['aio-pika>=8.1.1,<9.0.0']

setup_kwargs = {
    'name': 'coney',
    'version': '0.1.2',
    'description': 'Pika based rabbitmq client library',
    'long_description': None,
    'author': 'Teslim Olunlade',
    'author_email': 'tolunlade@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
