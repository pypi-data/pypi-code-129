# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['md_sign']

package_data = \
{'': ['*']}

install_requires = \
['signxml>=2.9.0,<3.0.0', 'typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['md-sign = md_sign.main:cli']}

setup_kwargs = {
    'name': 'md-sign',
    'version': '0.1.0',
    'description': 'Script to sign metadata',
    'long_description': None,
    'author': 'Ivan Kanakarakis',
    'author_email': 'ivan.kanak@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
