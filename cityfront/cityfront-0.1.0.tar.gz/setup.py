# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cityfront',
 'cityfront.auth',
 'cityfront.cache',
 'cityfront.generator',
 'cityfront.generator.parsers',
 'cityfront.generator.parsers.endpoints',
 'cityfront.generator.parsers.schemas',
 'cityfront.rest',
 'cityfront.services']

package_data = \
{'': ['*'],
 'cityfront': ['templates/client/*',
               'templates/models/*',
               'templates/namespace/*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'PyJWT>=2.4.0,<3.0.0',
 'anyio>=3.6.1,<4.0.0',
 'appwrite>=0.10.0,<0.11.0',
 'asynctest>=0.13.0,<0.14.0',
 'blue>=0.9.1,<0.10.0',
 'datamodel-code-generator>=0.13.0,<0.14.0',
 'devtools>=0.9.0,<0.10.0',
 'diskcache>=5.4.0,<6.0.0',
 'httpx>=0.23.0,<0.24.0',
 'inflection>=0.5.1,<0.6.0',
 'jsonpointer>=2.3,<3.0',
 'loguru>=0.6.0,<0.7.0',
 'mimesis>=6.0.0,<7.0.0',
 'openapi-schema-pydantic>=1.2.4,<2.0.0',
 'snoop>=0.4.1,<0.5.0',
 'stringcase>=1.2.0,<2.0.0',
 'toolz>=0.12.0,<0.13.0',
 'typer[all]>=0.6.1,<0.7.0',
 'vcrpy>=4.2.0,<5.0.0']

setup_kwargs = {
    'name': 'cityfront',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Kevin H.',
    'author_email': 'kevin@autoworkz.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
