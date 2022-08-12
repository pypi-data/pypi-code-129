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
    'version': '0.1.1',
    'description': 'Terminal Widgets.',
    'long_description': "\n# Twidge\n\nSimple terminal widgets for simple people.\n\nThis package is mostly intended for my own personal use, but have at it.\n\n\n## Quick Start\n\n#### Echo Keypresses\n\n```sh\n  python -m twidge echo\n```\n\n```python\n  from twidge import echoers\n\n  echoers.echobytes()\n```\n\n#### Text Editor\n\n```sh\n  python -m twidge edit 'Hello World'\n```\n\n```python\n  from twidge import editors\n\n  content = editors.editstr('Hello World!')\n```\n\n#### Dictionary Editor\n\n```sh\n  python -m twidge editdict name,email,username,password\n```\n\n```python\n  from twidge import editors\n\n  favorite_colors = {'Alice': 'red', 'Bob': 'blue'}\n  content = editors.editdict(favorite_colors)\n```\n",
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
