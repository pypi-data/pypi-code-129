# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['auve']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'auve',
    'version': '22.8.9',
    'description': 'Simple tool for automatic version number generation',
    'long_description': '# auve\n\nauve is a very simple Python tool to provide auto-generated version texts that can be used as version numbers in any Python project.\n\n## Installation\n\nUse the package manager [pip](https://pip.pypa.io/en/stable/) to install auve.\n\n```bash\npip install auve\n```\n\n## Usage\n\nIn it\'s simplest form use it like so:\n\n```python\nfrom auve import AutoVersionNumber\n\n# returns a version number like "22.8.0"\nprint(AutoVersionNumber().version)\n\n# returns a build text like "22.308.1100"\nprint(AutoVersionNumber().build)\n\n# returns a release text like "2022-08-11"\nprint(AutoVersionNumber().release)\n\n# returns a full version number like\n# "version: 22.8.0, build_22.308.1100, release 2022-08-11"\nprint(AutoVersionNumber().full_version)\n```\n\n\'auve\' comes from \'AUtomatic VEersionnumber\' and therefor is an update method that will automatically update the version number - but this works with version files only, so it is also possible to store a version number in a file. Provide a file name and it will get created in the CWD.\n\n```python\nfrom auve import AutoVersionNumber\n\n# there are no rules for the file name, something like \'.version\' or \'VERSION\' seems fine\n# this file will by default be created in the CWD\nfile = "DEMO_VERSION"\n# relative paths are also possible\n# if the provided path not exists it also gets created\nfile = "./foo/DEMO_VERSION"\n\n# date: 2022-08-11\n# day of year: 308\n# time: 11:00\n# if there is no file auve creates it\n# returns something like: "22.8.0"\nprint(AutoVersionNumber(file))\n\n# returns a build number like "22.308.1100", from file\nprint(AutoVersionNumber(file).build)\n\n# returns a release number like "2022-08-11", from file\nprint(AutoVersionNumber(file).release)\n\n# returns a full version number like\n# "version: 22.8.0, build_22.308.1100, release 2022-08-11", from file\nprint(AutoVersionNumber(file).full_version)\n```\n\nThe parts of the version text are simply generated from the actual date and time when using the tool.\nThe update method updates the version number depending on the month, eg. if it is August in 2022, the version number uses \'22\' and \'08\' as primary and secondary parts of the version number. When initializing a version for the first time, the third part (one could see this as \'micro\' or \'patch\' part) will be set to \'0\'. When updating this version number from a file, this \'micro\' or \'patch\' part will be increased by \'1\' - as long as the year is still \'22\' and the month is still \'08\' in this particular example. If not, these parts also will be updated to the actual year and month and \'micro\'/\'patch\' will again be set to \'0\'.\nThe \'build\' and \'release\' strings also depend on the actual date and time, when doing the update.\n\n```python\n# date: 2022-08-15\n# day of year: 312\n# time: 16:30\n# returns "True"\nprint(AutoVersionNumber(file).update())\n\n# returns a full version number like\n# "version: 22.8.1, build_22.312.1630, release 2022-08-15", from file\nprint(AutoVersionNumber(file).full_version)\n```\n\n## Demo\n\nThere is also a simple demo module in the package:\n\n```python\nfrom auve import demo\n\ndemo()\n```\n\nPlease take note that when running this demo script a file named "DEMO_VERSION" will be generated in the CWD. This file is just for demonstration purposes and can be deleted after running the demo.\n\n## License\n\n[MIT](https://choosealicense.com/licenses/mit/)\n',
    'author': 'Marc Scoop',
    'author_email': 'marc.scoop@bitmarc.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
