# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['esi_utils_colors']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.1.0', 'numpy>=1.21', 'pandas>=1.0']

extras_require = \
{'dev': ['black>=21', 'flake8>=3.9', 'ipython>=7.26'], 'tests': ['pytest>=6.2']}

setup_kwargs = {
    'name': 'esi-utils-colors',
    'version': '1.0.3',
    'description': 'USGS Earthquake Impact Utilities for Colors',
    'long_description': None,
    'author': 'Mike Hearne',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>3.8',
}


setup(**setup_kwargs)
