# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pleiotropy']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pleiotropy',
    'version': '0.1.1',
    'description': '',
    'long_description': '# pleiotropy\n\n> Automate Singe Cell Data Pipelines\n\n[![PyPI version][pypi-image]][pypi-url]\n[![Build status][build-image]][build-url]\n[![Code coverage][coverage-image]][coverage-url]\n[![GitHub stars][stars-image]][stars-url]\n[![Supported Python versions][versions-image]][versions-url]\n\n\n...\n\n<!-- Badges: -->\n\n[pypi-image]: https://img.shields.io/pypi/v/pleiotropy\n[pypi-url]: https://pypi.org/project/pleiotropy/\n[build-image]: https://github.com/jlikhuva/pleiotropy/actions/workflows/build.yaml/badge.svg\n[build-url]: https://github.com/jlikhuva/pleiotropy/actions/workflows/build.yaml\n[coverage-image]: https://codecov.io/gh/jlikhuva/pleiotropy/branch/main/graph/badge.svg\n[coverage-url]: https://codecov.io/gh/jlikhuva/pleiotropy/\n[stars-image]: https://img.shields.io/github/stars/jlikhuva/pleiotropy\n[stars-url]: https://github.com/jlikhuva/pleiotropy\n[versions-image]: https://img.shields.io/pypi/pyversions/pleiotropy\n[versions-url]: https://pypi.org/project/pleiotropy/\n',
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
