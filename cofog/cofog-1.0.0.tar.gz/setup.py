# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cofog']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.1']

entry_points = \
{'console_scripts': ['cofog = cofog.__main__:main']}

setup_kwargs = {
    'name': 'cofog',
    'version': '1.0.0',
    'description': 'Cofog',
    'long_description': '# Cofog\n\n[![PyPI](https://img.shields.io/pypi/v/cofog.svg)][pypi_]\n[![Status](https://img.shields.io/pypi/status/cofog.svg)][status]\n[![Python Version](https://img.shields.io/pypi/pyversions/cofog)][python version]\n[![License](https://img.shields.io/pypi/l/cofog)][license]\n\n[![Read the documentation at https://cofog.readthedocs.io/](https://img.shields.io/readthedocs/cofog/latest.svg?label=Read%20the%20Docs)][read the docs]\n[![Tests](https://github.com/oliverjwroberts/cofog/workflows/Tests/badge.svg)][tests]\n[![Codecov](https://codecov.io/gh/oliverjwroberts/cofog/branch/main/graph/badge.svg)][codecov]\n\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]\n\n[pypi_]: https://pypi.org/project/cofog/\n[status]: https://pypi.org/project/cofog/\n[python version]: https://pypi.org/project/cofog\n[read the docs]: https://cofog.readthedocs.io/\n[tests]: https://github.com/oliverjwroberts/cofog/actions?workflow=Tests\n[codecov]: https://app.codecov.io/gh/oliverjwroberts/cofog\n[pre-commit]: https://github.com/pre-commit/pre-commit\n[black]: https://github.com/psf/black\n\n## Introduction\n\nClassification of the Functions of Government (COFOG) is a classification defined by the United Nations Statistics Division. Its purpose is to "classify the purpose of transactions such as outlays on final consumption expenditure, intermediate consumption, gross capital formation and capital and current transfers, by general government" (from [home page]).\n\nThis intention of this package is to serve a convenient way of parsing and interfacing with the classifications.\n\n## Data\n\nData was sourced from the UN\'s [classifications on economic statistics page] and parsed into a dictionary that can be found in `src/cofog/data.py`.\n\n## Features\n\n- Provides the `COFOG` class to represent a Classification of Functions of Government.\n- Validate `COFOG` codes through Regular Expressions and presence in the data.\n- Lookup descriptions from codes.\n- Traverse the levels of any given code, with the ability to set a lower level without forgetting the original level.\n\n## Requirements\n\n- Python >=3.7\n- Click >=8.0.1\n\n## Installation\n\nYou can install _Cofog_ via [pip] from [PyPI]:\n\n```console\n$ pip install cofog\n```\n\n## Usage\n\nPlease see the [usage page] in the docs for full details.\n\nGet started by initialising a new `COFOG` object with a code. These can be either specified as strings (with and without dots) or integers.\n\n```python\nfrom cofog import COFOG\n\ncofog = COFOG("04.3.6")\n\n# or any of the following\nCOFOG("0436")\nCOFOG("436")\nCOFOG(436)\n```\n\nYou can then access the code\'s description as well as traverse it\'s levels.\n\n```python\nprint(cofog.description)\n# Non-electric energy  (CS)\nprint(cofog.level)\n# 3\n\ncofog.set_level(2)\nprint(cofog.code)\n# 04.3\nprint(cofog.description)\n# Fuel and energy\n```\n\n## Contributing\n\nContributions are very welcome.\nTo learn more, see the [Contributor Guide].\n\n## License\n\nDistributed under the terms of the [MIT license][license],\n_Cofog_ is free and open source software.\n\n## Issues\n\nIf you encounter any problems,\nplease [file an issue] along with a detailed description.\n\n## Credits\n\nThis project was heavily inspired by [@ellsphillips]\'s [govsic] package.\n\nThis project was generated from [@cjolowicz]\'s [Hypermodern Python Cookiecutter] template.\n\n[home page]: https://unstats.un.org/unsd/classifications/Family/Detail/4\n[classifications on economic statistics page]: https://unstats.un.org/unsd/classifications/Econ\n[pip]: https://pip.pypa.io/\n[pypi]: https://pypi.org/\n[@ellsphillips]: https://github.com/ellsphillips\n[govsic]: https://github.com/ellsphillips/govsic\n[@cjolowicz]: https://github.com/cjolowicz\n[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n[file an issue]: https://github.com/oliverjwroberts/cofog/issues\n\n<!-- github-only -->\n\n[usage page]: https://cofog.readthedocs.io/en/latest/usage.html\n[contributor guide]: https://github.com/oliverjwroberts/cofog/blob/main/CONTRIBUTING.md\n[license]: https://github.com/oliverjwroberts/cofog/blob/main/LICENSE\n',
    'author': 'Oliver Roberts',
    'author_email': 'oliverjwroberts@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/oliverjwroberts/cofog',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
