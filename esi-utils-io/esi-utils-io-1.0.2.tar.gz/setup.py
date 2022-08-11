# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['esi_utils_io']

package_data = \
{'': ['*']}

install_requires = \
['h5py>=3.1.0', 'numpy>=1.21', 'pandas>=1.0', 'pytz>=2021.3']

extras_require = \
{'dev': ['black>=21', 'flake8>=3.9', 'ipython>=7.26'], 'tests': ['pytest>=6.2']}

setup_kwargs = {
    'name': 'esi-utils-io',
    'version': '1.0.2',
    'description': 'USGS Earthquake Impact Utilities for IO',
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
