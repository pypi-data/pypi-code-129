# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['img2pdfscrpr']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.2.0,<10.0.0',
 'beautifulsoup4>=4.11.1,<5.0.0',
 'pathlib>=1.0.1,<2.0.0',
 'requests>=2.28.1,<3.0.0']

entry_points = \
{'console_scripts': ['img2pdfscrpr = img2pdfscrpr.img2pdfscrpr:main']}

setup_kwargs = {
    'name': 'img2pdfscrpr',
    'version': '0.1',
    'description': 'Image to PDF Web Scraper (tailored for Manga)',
    'long_description': None,
    'author': 'paytonward6',
    'author_email': '72841140+paytonward6@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
