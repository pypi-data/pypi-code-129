# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['velovi']

package_data = \
{'': ['*']}

install_requires = \
['anndata>=0.7.5', 'scikit-learn>=0.21.2', 'scvelo', 'scvi-tools>=0.16.4']

extras_require = \
{':(python_version < "3.8") and (extra == "docs")': ['typing_extensions'],
 ':python_version < "3.8"': ['importlib-metadata>=1.0,<2.0'],
 'dev': ['black>=20.8b1',
         'codecov>=2.0.8',
         'flake8>=3.7.7',
         'isort>=5.7',
         'jupyter>=1.0',
         'nbconvert>=5.4.0',
         'nbformat>=4.4.0',
         'pre-commit>=2.7.1',
         'pytest>=4.4',
         'scanpy>=1.6'],
 'docs': ['ipython>=7.1.1',
          'nbsphinx',
          'nbsphinx-link',
          'pydata-sphinx-theme>=0.4.0',
          'scanpydoc>=0.5',
          'sphinx>=4.1',
          'sphinx-autodoc-typehints',
          'sphinx-rtd-theme'],
 'tutorials': ['scanpy>=1.6']}

setup_kwargs = {
    'name': 'velovi',
    'version': '0.1.0',
    'description': 'Estimation of RNA velocity with variational inference.',
    'long_description': '# velovi\n\n[![Stars](https://img.shields.io/github/stars/YosefLab/velovi?logo=GitHub&color=yellow)](https://github.com/YosefLab/velovi/stargazers)\n[![Documentation Status](https://readthedocs.org/projects/velovi/badge/?version=latest)](https://velovi.readthedocs.io/en/stable/?badge=stable)\n![Build Status](https://github.com/YosefLab/velovi/workflows/velovi/badge.svg)\n[![codecov](https://codecov.io/gh/YosefLab/velovi/branch/main/graph/badge.svg?token=BGI9Z8R11R)](https://codecov.io/gh/YosefLab/velovi)\n[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)\n\nVariational inference for RNA velocity. This is an experimental repo for the veloVI model. Installation instructions and tutorials are in the docs. Over the next few months veloVI will move into [scvi-tools](https://scvi-tools.org/), and wrappers wil be built in [scVelo](https://scvelo.org/).\n',
    'author': 'Adam Gayoso',
    'author_email': 'adamgayoso@berkeley.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/YosefLab/velovi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
