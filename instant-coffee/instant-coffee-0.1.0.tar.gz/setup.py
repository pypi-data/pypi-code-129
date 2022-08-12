# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['instantcoffee',
 'instantcoffee.cloudcredentials',
 'instantcoffee.kaffeeservice']

package_data = \
{'': ['*']}

install_requires = \
['Faker',
 'connect-extension-runner>=25.0.0,<26.0.0',
 'cryptography>=37.0.2,<38.0.0',
 'extaasy>=0.1.0,<0.2.0',
 'mock>=4.0.3,<5.0.0',
 'pyjwt>=2.4.0,<3.0.0',
 'pytest>=7.1.2,<8.0.0',
 'responses>=0.20.0,<0.21.0']

setup_kwargs = {
    'name': 'instant-coffee',
    'version': '0.1.0',
    'description': 'Project description',
    'long_description': '# Instant Coffee\n\nA library for connecting to kaffeeservice in Instant Cloud Solutions\n',
    'author': 'Ingram Micro Inc.',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
