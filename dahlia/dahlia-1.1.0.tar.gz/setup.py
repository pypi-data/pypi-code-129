# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['dahlia']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['dahlia = dahlia.__main__:main']}

setup_kwargs = {
    'name': 'dahlia',
    'version': '1.1.0',
    'description': 'A library allowing you to use Minecraft format codes in strings.',
    'long_description': None,
    'author': 'trag1c',
    'author_email': 'trag1cdev@yahoo.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/trag1c/Dahlia',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
