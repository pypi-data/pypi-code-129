# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['jenesis',
 'jenesis.cmd',
 'jenesis.cmd.add',
 'jenesis.cmd.alpha',
 'jenesis.cmd.alpha.keys',
 'jenesis.config',
 'jenesis.contracts',
 'jenesis.keyring',
 'jenesis.keyring.amino',
 'jenesis.keyring.infos',
 'jenesis.keyring.macos',
 'jenesis.tasks']

package_data = \
{'': ['*']}

install_requires = \
['blessings>=1.7,<2.0',
 'cosmpy>=0.5.1,<0.6.0',
 'docker>=5.0.3,<5.1.0',
 'mkdocs-material>=8.3.9,<9.0.0',
 'mkdocs>=1.3.1,<2.0.0',
 'ptpython>=3.0.20,<4.0.0',
 'toml>=0.10.2,<0.11.0',
 'tqdm>=4.64.0,<5.0.0']

entry_points = \
{'console_scripts': ['jenesis = jenesis.cli:main']}

setup_kwargs = {
    'name': 'jenesis',
    'version': '0.1.1',
    'description': '',
    'long_description': 'Jenesis is a command line tool for rapid contract and service development for CosmWasm-enabled blockchains.\n\n# Installation\n\nInstall jenesis for Python 3.7 or newer via PyPI:\n\n```\npip install jenesis\n```\n\n# Getting started\n\n## Create a new project\n\n```\njenesis new my_project\n```\n\n## Initialize jenesis in an existing project directory\n\n```\njenesis init\n```\n\n## Compile contracts\n\n\n```\njenesis compile\n```\n',
    'author': 'Ed FitzGerald',
    'author_email': 'edward.fitzgerald@fetch.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
