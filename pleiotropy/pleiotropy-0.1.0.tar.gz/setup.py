# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pleiotropy']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pleiotropy',
    'version': '0.1.0',
    'description': '',
    'long_description': '# pleiotropy\n\nAutomate Singe Cell Data Pipelines\n\n[![Build Status][build-image]][build-url]\n[![Code Coverage][coverage-image]][coverage-url]\n[![Python Versions][versions-image]][versions-url]\n\n...\n\n<!-- Badges: -->\n\n[build-image]: https://github.com/jlikhuva/pleiotropy/actions/workflows/build.yaml/badge.svg\n[build-url]: https://github.com/jlikhuva/pleiotropy/actions/workflows/build.yaml\n[coverage-image]: https://codecov.io/gh/jlikhuva/pleiotropy/branch/main/graph/badge.svg\n[coverage-url]: https://codecov.io/gh/jlikhuva/pleiotropy/\n[versions-image]: https://img.shields.io/pypi/pyversions/pleiotropy/\n[versions-url]: https://pypi.org/project/pleiotropy/\n',
    'author': 'jlikhuva',
    'author_email': 'jlikhuva@alumni.stanford.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
