# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['twidge']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.4.2,<2.0.0',
 'rich>=12.5.1,<13.0.0',
 'typer>=0.6.1,<0.7.0',
 'xlrd>=2.0.1,<3.0.0']

entry_points = \
{'console_scripts': ['twidge = twidge.cli:cli']}

setup_kwargs = {
    'name': 'twidge',
    'version': '0.1.0',
    'description': 'Terminal Widgets.',
    'long_description': None,
    'author': 'Aidan Courtney',
    'author_email': 'aidanfc97@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
