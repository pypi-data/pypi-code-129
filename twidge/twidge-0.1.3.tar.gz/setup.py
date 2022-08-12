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
    'version': '0.1.3',
    'description': 'Terminal Widgets.',
    'long_description': "\n# Twidge\n\nSimple terminal widgets for simple people.\n\nThis package is mostly intended for my own personal use, but have at it.\n\n\n## Quick Start\n\n#### Install\n\n```sh\npython -m pip install twidge\n```\n\n#### Echo Keypresses\n\n```sh\npython -m twidge echo\n```\n\n```python\nfrom twidge import echoers\n\nechoers.echobytes()\n```\n\n#### Text Editor\n\n```sh\npython -m twidge edit 'Hello World'\n```\n\n```python\nfrom twidge import editors\n\ncontent = editors.editstr('Hello World!')\n```\n\n#### Dictionary Editor\n\n```sh\npython -m twidge editdict name,email,username,password\n```\n\n```python\nfrom twidge import editors\n\nfavorite_colors = {'Alice': 'red', 'Bob': 'blue'}\ncontent = editors.editdict(favorite_colors)\n```\n\n## Issues\n\nMany.\n",
    'author': 'Aidan Courtney',
    'author_email': 'aidanfc97@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/aidaco/twidge',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
