# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['singlue']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['singlue = singlue.main:main']}

setup_kwargs = {
    'name': 'singlue',
    'version': '0.1.2',
    'description': '',
    'long_description': None,
    'author': 'kawagh',
    'author_email': 'kawagh@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
