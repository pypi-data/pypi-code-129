# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['testing_absolute_imports']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'testing-absolute-imports',
    'version': '0.1.0',
    'description': 'Personal project to test absolute importing inside a distribution package',
    'long_description': None,
    'author': 'Yashesh Dasari',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
