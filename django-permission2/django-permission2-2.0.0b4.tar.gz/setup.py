# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['src',
 'src.permission',
 'src.permission.decorators',
 'src.permission.logics',
 'src.permission.templatetags',
 'src.permission.tests',
 'src.permission.tests.test_decorators',
 'src.permission.tests.test_logics',
 'src.permission.tests.test_templatetags',
 'src.permission.tests.test_utils',
 'src.permission.utils']

package_data = \
{'': ['*']}

install_requires = \
['app_version>=1.0.1,<2.0.0', 'django-appconf>=1.0.5,<2.0.0']

extras_require = \
{'docs': ['Sphinx==5.1.1', 'sphinx-rtd-theme==1.0.0']}

setup_kwargs = {
    'name': 'django-permission2',
    'version': '2.0.0b4',
    'description': 'A simple permission system which enable logical permission systems in Django',
    'long_description': None,
    'author': 'Malte Gerth',
    'author_email': 'mail@malte-gerth.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
