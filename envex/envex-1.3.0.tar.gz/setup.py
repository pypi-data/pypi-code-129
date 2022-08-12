# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['envex']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'envex',
    'version': '1.3.0',
    'description': 'An extended and convenient os.environ interface',
    'long_description': '************\nenv exTENDED\n************\n\ndotenv `.env` aware environment variable handling with typing features\n\nOverview\n--------\n\nThis is a refactoring of django-settings-env with Django specific functionality stripped out,\nand so implements all of the smart environment handling suitable for use outside of Django.\n\nThis module provides a convenient interface for handling the environment, and therefore\nconfiguration of any application using 12factor.net principals removing many environment specific\nvariables and security sensitive information from application code.\n\nThis module provides some features not supported by other dotenv handlers\n(python-dotenv, etc.) including expansion of template variables which is very useful\nfor DRY.\n\nAn `Env` instance delivers a lot of functionality by providing a type-smart\nfront-end to `os.environ`, with support for most - if not all - `os.environ` functionality.\n```python\nfrom envex import env\n\nassert env[\'HOME\'] ==  \'/Users/davidn\'\nenv[\'TESTING\'] = \'This is a test\'\nassert env[\'TESTING\'] == \'This is a test\'\n\nimport os\nassert os.environ[\'TESTING\'] == \'This is a test\'\n\nassert env.get(\'UNSET_VAR\') is None\nenv.set(\'UNSET_VAR\', \'this is now set\')\nassert env.get(\'UNSET_VAR\') is not None\nenv.setdefault(\'UNSET_VAR\', \'and this is a default value but only if not set\')\nassert env.get(\'UNSET_VAR\') == \'this is now set\'\ndel env[\'UNSET_VAR\']\nassert env.get(\'UNSET_VAR\') is None\n```\n\nAn Env instance can also read a `.env` (default name) file and update the\napplication environment accordingly.\n\nIt can read this either from `__init__` or via the method `read_env()`.\n\n* Override the base name of the dot env file, use the `DOTENV` environment variable.\n* Other kwargs that can be passed to `Env.__init__`\n\n  * env_file (str): base name of the env file, os.environ["DOTENV"] by default, or .env\n  * search_path (str or list): a single path or list of paths to search for the env file\n  * overwrite (bool): overwrite already set values read from .env, default is to only set if not currently set\n  * parents (bool): search (or not) parents of dirs in the search_path\n  * update (bool): update os.environ if true (default) otherwise pool changes internally\n  * environ (env): pass the environment to update, default is os.environ\n\n* Env() also takes an additional kwarg, `readenv` (default False) which instructs it to read dotenv files\n\n\n\nSome type-smart functions act as an alternative to `Env.get` and having to\nparse the result:\n```python\nfrom envex import env\n\nenv[\'AN_INTEGER_VALUE\'] = 2875083\nassert env.get(\'AN_INTEGER_VALUE\') == \'2875083\'\nassert env.int(\'AN_INTEGER_VALUE\') == 2875083\n\nenv[\'A_TRUE_VALUE\'] = True\nassert env.get(\'A_TRUE_VALUE\') == \'True\'\nassert env.bool(\'A_TRUE_VALUE\') is True\n\nenv[\'A_FALSE_VALUE\'] = 0\nassert env.get(\'A_FALSE_VALUE\') == \'0\'\nassert env.int(\'A_FALSE_VALUE\') == 0\nassert env.bool(\'A_FALSE_VALUE\') is False\n\nenv[\'A_FLOAT_VALUE\'] = 287.5083\nassert env.get(\'A_FLOAT_VALUE\') == \'287.5083\'\nassert env.float(\'A_FLOAT_VALUE\') == 287.5083\n\nenv[\'A_LIST_VALUE\'] = \'1,"two",3,"four"\'\nassert env.get(\'A_LIST_VALUE\') == \'1,"two",3,"four"\'\nassert env.list(\'A_LIST_VALUE\') == [\'1\', \'two\', \'3\', \'four\']\n```\n\nNote that environment variables are always stored as strings. This is\nenforced by the underlying os.environ, but also also true of any provided\nenvironment, using the `MutableMapping[str, str]` contract.\n',
    'author': 'David Nugent',
    'author_email': 'davidn@uniquode.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
