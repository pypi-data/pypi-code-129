# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['marko_namo']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'marko-namo',
    'version': '0.3.0',
    'description': 'Markov chain project name generator',
    'long_description': '# Marko-Namo\n\n\n![PyPi Version](https://img.shields.io/pypi/v/marko-namo)\n![Python Versions](https://img.shields.io/pypi/pyversions/marko-namo)\n[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)\n<br/>\n\n[![Code Hygiene](https://github.com/diabolical-ninja/Marko-Namo/actions/workflows/code_hygiene.yml/badge.svg)](https://github.com/diabolical-ninja/Marko-Namo/actions/workflows/code_hygiene.yml)\n[![codecov](https://codecov.io/gh/diabolical-ninja/Marko-Namo/branch/main/graph/badge.svg?token=Q4zU40ENrt)](https://codecov.io/gh/diabolical-ninja/Marko-Namo)\n![black codestyle](https://img.shields.io/badge/Code%20Style-Black-black)\n<br/>\n\n[![Documentation Status](https://readthedocs.org/projects/marko-namo/badge/?version=latest)](https://marko-namo.readthedocs.io/en/latest/?badge=latest)\n\n<br/>\n\n\nSimple tool to generate random project or business names using a basic [Markov Chain](https://en.wikipedia.org/wiki/Markov_chain) approach.\n\n\n## Installation\n\nInstall `marko-namo` from the Python Package Index:\n\n```console\n$ pip install marko-namo\n```\n\n## Requirements\n\n- Python 3.8+\n\n\n## How It Words\n\nThe generator starts by creating a frequency table based on the training words supplied and the n-grams listed. Eg if our training word is `hello` and our n-grams are 1 and 2, we\'d get a frequency table of:\n```json\n{\n    "h": ["e", "el"],\n    "he": ["l", "ll"],\n    "e": ["l", "ll"],\n    "el": ["l", "lo"],\n    "l": ["l", "lo", "o", null],\n    "ll": ["o", null],\n    "lo": [null, null],\n    "o": [null, null]\n}\n```\n\nIt then randomly selects an n-gram from the frequency table as the first letter, randomly selects a following letter and repeats until the word either ends (selects a `None`) or reaches the maximum word length.\n\nEg if the first selected letter was `e` we might go:\n- `e` -> `l` -> `lo` -> None\n- Which gives `ello`\n\n\n## How To Run\n\nYou can either create a config file and pass that in or specifiy your parameters in code. To get started, you can utilse the `config_sample.yml`.\n\n```python\nfrom marko_namo import MarkoNamo\n\nrandom_name_generator = MarkoNamo("config_sample.yml")\ncreated_names, available_domains = random_name_generator.create_random_names()\n```\n\nIf you\'d rather not use a config file then you can run:\n```python\nfrom marko_namo import MarkoNamo\n\nrandom_name_generator = MarkoNamo(\n    name_length = 5,\n    number_of_names = 10,\n    training_words = ["hello", "pineapple", "planet"]\n)\ncreated_names, available_domains = random_name_generator.create_random_names()\n\n```\n\n### Parameters\n\n| Parameter \t| Type \t| Description \t|\n|---\t|---\t|---\t|\n| `number_of_names` \t| Integer \t| Number of names to attempt to create \t|\n| `maximum_name_length` \t| Integer \t| Maximum name length. Note names can be up to length + largest n-gram in length \t|\n| `n_grams` \t| List of integers \t| The word segment lengths to consider for learning and generating new words. \t|\n| `extensions` \t| List of strings \t| Domain extensions to check for such as `.com`, `.ai`, etc \t|\n| `training_words` \t| List of strings \t| Words to learn from and used to generate new, random, words.  There\'s no limit to the number of words to learn from but too many will slow the program down significantly. \t|\n\n\n### Domain Name Lookup\nIf you\'d like to check if the domain name (eg `www.randomname.com`) is available for the generated names then you\'ll also need a GoDaddy API key. This can be generated at the following: https://developer.godaddy.com/keys\n\nYou\'ll need to provide:\n- API Key\n- API Secret\n- Whether you\'d like to use their OTE (test) or PROD (production) environment\n\n\n## Building the Project\n\nThis package uses `poetry` and `nox` for package management and building. \n\nIf nox is not already installed, install it:\n```console\n$ pip install nox\n$ pip install nox_poetry\n```\n\nRun everything including tests and documentation building\n```console\n$ nox\n\n# Or to run a specific stage:\n$ nox -s <stage name>, eg\n$ nox -s tests\n```\n\n## Testing\n\nNox also handles the tests but you\'ll require OTE & PROD keys to run the GoDaddy tests.\n\n1. Register with GoDaddy and generate OTE & PROD keys\n2. Set them as environment variables:\n```sh\n# GoDaddy OTE\nGODADDY_OTE_KEY=<OTE Key>\nGODADDY_OTE_SECRET=<OTE Secret>\nGODADDY_OTE_ENV=OTE\n\n# GoDaddy Prod\nGODADDY_PROD_KEY=<Prod Key>\nGODADDY_PROD_SECRET=<Prod Secret>\nGODADDY_PROD_ENV=PROD\n```\n\n3. Run the tests:\n```console\n$ nox -s tests\n```\n\n## Issues\n\nIf you encounter any problems, please [file an issue](https://github.com/diabolical-ninja/Marko-Namo/issues) along with a detailed description.\n',
    'author': 'Yass Eltahir',
    'author_email': '15998949+diabolical-ninja@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/diabolical-ninja/Marko-Namo',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
