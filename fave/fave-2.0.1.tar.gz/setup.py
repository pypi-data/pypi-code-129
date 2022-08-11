# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fave', 'fave.align', 'fave.align.model', 'fave.extract']

package_data = \
{'': ['*'],
 'fave': ['praatScripts/*'],
 'fave.align': ['examples/*', 'examples/test/*', 'old_docs/*', 'readme_img/*'],
 'fave.align.model': ['11025/*',
                      '16000 (old model)/*',
                      '16000/*',
                      '8000/*',
                      'backups dicts/*',
                      'g-dropping Jiahong/*',
                      'g-dropping Jiahong/16000/*'],
 'fave.extract': ['config/*', 'old_docs/*']}

install_requires = \
['numpy>=1.22,<2.0', 'tqdm>=4.64.0,<5.0.0']

entry_points = \
{'console_scripts': ['FAAValign = fave.FAAValign:setup',
                     'extractFormants = fave.extractFormants:main']}

setup_kwargs = {
    'name': 'fave',
    'version': '2.0.1',
    'description': 'Forced alignment and vowel extraction',
    'long_description': None,
    'author': 'FAVE contributors',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
