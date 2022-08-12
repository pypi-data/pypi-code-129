# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyseafuel']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.21.1,<2.0.0', 'pdoc>=12.0.2,<13.0.0', 'scipy>=1.7.1,<2.0.0']

setup_kwargs = {
    'name': 'pyseafuel',
    'version': '0.1.1',
    'description': 'Package to numerically model a methanol producing island.',
    'long_description': None,
    'author': 'Doug Keller',
    'author_email': 'dg.kllr.jr@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.10',
}


setup(**setup_kwargs)
