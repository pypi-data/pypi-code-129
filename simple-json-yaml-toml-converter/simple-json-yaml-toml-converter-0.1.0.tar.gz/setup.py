# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simple_json_yaml_toml_converter']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0', 'click>=8.1.3,<9.0.0', 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['simple-json-yaml-toml-converter = '
                     'simple_json_yaml_toml_converter.cli:command']}

setup_kwargs = {
    'name': 'simple-json-yaml-toml-converter',
    'version': '0.1.0',
    'description': 'Simple json/yaml/toml CLI converter.',
    'long_description': None,
    'author': '0djentd',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
