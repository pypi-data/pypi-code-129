# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['img2pdfscrpr', 'img2pdfscrpr.src', 'img2pdfscrpr.tests']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.2.0,<10.0.0',
 'beautifulsoup4>=4.11.1,<5.0.0',
 'pathlib>=1.0.1,<2.0.0',
 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'img2pdfscrpr',
    'version': '0.0.2',
    'description': 'Download images, and convert to PDF for side-by-side reading (optimized for manga)',
    'long_description': None,
    'author': 'Payton Ward',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
