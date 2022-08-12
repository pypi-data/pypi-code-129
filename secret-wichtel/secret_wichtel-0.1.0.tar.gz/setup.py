# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['secret_wichtel']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.1,<2.0.0']

setup_kwargs = {
    'name': 'secret-wichtel',
    'version': '0.1.0',
    'description': 'Secret Santa script for your christmas pleasure.',
    'long_description': None,
    'author': 'danczw',
    'author_email': 'dev.dc@pm.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
