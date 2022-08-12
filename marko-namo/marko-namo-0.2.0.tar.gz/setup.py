# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

modules = \
['marko_namo']
install_requires = \
['PyYAML>=6.0,<7.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'marko-namo',
    'version': '0.2.0',
    'description': 'Markov chain project name generator',
    'long_description': '# Marko-Namo\n\n[![codecov](https://codecov.io/gh/diabolical-ninja/RandomNameGenerator/branch/main/graph/badge.svg?token=Q4zU40ENrt)](https://codecov.io/gh/diabolical-ninja/RandomNameGenerator)\n[![Linting and Unit Tests](https://github.com/diabolical-ninja/RandomNameGenerator/actions/workflows/hygiene_checks.yml/badge.svg)](https://github.com/diabolical-ninja/RandomNameGenerator/actions/workflows/hygiene_checks.yml)\n\nSimple tool to generate random project or business names using a basic [Markov Chain](https://en.wikipedia.org/wiki/Markov_chain) approach.\n\n## How It Words\n\nThe generator starts by creating a frequency table based on the training words supplied and the n-grams listed. Eg if our training word is `hello` and our n-grams are 1 and 2, we\'d get a frequency table of:\n```json\n{\n    "h": ["e", "el"],\n    "he": ["l", "ll"],\n    "e": ["l", "ll"],\n    "el": ["l", "lo"],\n    "l": ["l", "lo", "o", null],\n    "ll": ["o", null],\n    "lo": [null, null],\n    "o": [null, null]\n}\n```\n\nIt then randomly selects an n-gram from the frequency table as the first letter, randomly selects a following letter and repeats until the word either ends (selects a `None`) or reaches the maximum word length.\n\nEg if the first selected letter was `e` we might go:\n- `e` -> `l` -> `lo` -> None\n- Which gives `ello`\n\n\n## How To Run\n\nEverything is controlled via the configuration file (`config.yml`)\n\nTo get started, rename the `config_sample.yml` to `config.yml` and remove the GoDaddy references. Then run the app:\n```sh\npython generate_names.py\n```\n\n### Parameters\n\n| Parameter \t| Type \t| Description \t|\n|---\t|---\t|---\t|\n| `number_of_names` \t| Integer \t| Number of names to attempt to create \t|\n| `maximum_name_length` \t| Integer \t| Maximum name length. Note names can be up to length + largest n-gram in length \t|\n| `n_grams` \t| List of integers \t| The word segment lengths to consider for learning and generating new words. \t|\n| `extensions` \t| List of strings \t| Domain extensions to check for such as `.com`, `.ai`, etc \t|\n| `training_words` \t| List of strings \t| Words to learn from and used to generate new, random, words.  There\'s no limit to the number of words to learn from but too many will slow the program down significantly. \t|\n\n\n### Domain Name Lookup\nIf you\'d like to check if the domain name (eg `www.randomname.com`) is available for the generated names then you\'ll also need a GoDaddy API key. This can be generated at the following: https://developer.godaddy.com/keys\n\n\n\n## Testing\n\n[Nox](https://nox.thea.codes/en/stable/) is used handle test automation. To run the tests:\n\n1. Register with GoDaddy and generate OTE & PROD keys\n2. Set them as environment variables:\n```sh\n# GoDaddy OTE\nGODADDY_OTE_KEY=<OTE Key>\nGODADDY_OTE_SECRET=<OTE Secret>\n\n# GoDaddy Prod\nGODADDY_PROD_KEY=<Prod Key>\nGODADDY_PROD_SECRET=<Prod Secret>\n```\n3. Install [nox](https://nox.thea.codes/en/stable/) if not already available \n4. Run the tests:\n```sh\nnox\n```',
    'author': 'Yass Eltahir',
    'author_email': '15998949+diabolical-ninja@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/diabolical-ninja/Marko-Namo',
    'package_dir': package_dir,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
