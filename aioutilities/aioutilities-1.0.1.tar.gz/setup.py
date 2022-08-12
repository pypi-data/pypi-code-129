# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['aioutilities', 'aioutilities.pool']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['aioutilities-example = aioutilities.example:run_example']}

setup_kwargs = {
    'name': 'aioutilities',
    'version': '1.0.1',
    'description': 'asyncio-powered coroutine worker pool',
    'long_description': None,
    'author': 'Kevin Kirsche',
    'author_email': 'kev.kirsche@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4',
}


setup(**setup_kwargs)
