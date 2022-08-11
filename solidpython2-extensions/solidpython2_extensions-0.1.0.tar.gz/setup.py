# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['solid2_extensions', 'solid2_extensions.examples']

package_data = \
{'': ['*']}

install_requires = \
['solidpython2>=2.0.0-beta.1,<3.0.0']

setup_kwargs = {
    'name': 'solidpython2-extensions',
    'version': '0.1.0',
    'description': 'some extensions for solidpython2',
    'long_description': None,
    'author': 'jeff',
    'author_email': '1105041+jeff-dh@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
