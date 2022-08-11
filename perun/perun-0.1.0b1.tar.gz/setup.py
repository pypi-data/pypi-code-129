# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['perun', 'perun.backend']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'h5py>=3.7.0,<4.0.0',
 'mpi4py>=3.1.3,<4.0.0',
 'py-cpuinfo>=8.0.0,<9.0.0',
 'pyRAPL>=0.2.3,<0.3.0',
 'pynvml>=11.4.1,<12.0.0',
 'python-dotenv>=0.20.0,<0.21.0']

entry_points = \
{'console_scripts': ['perun = perun.cli:cli']}

setup_kwargs = {
    'name': 'perun',
    'version': '0.1.0b1',
    'description': '',
    'long_description': None,
    'author': 'Gutiérrez Hermosillo Muriedas, Juan Pedro',
    'author_email': 'juanpedroghm@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
