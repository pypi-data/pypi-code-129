# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['np_data_validator_2',
 'np_data_validator_2.builtins',
 'np_data_validator_2.dataclasses',
 'np_data_validator_2.lims',
 'np_data_validator_2.transformers',
 'np_data_validator_2.validation_plan']

package_data = \
{'': ['*']}

install_requires = \
['marshmallow>=3.17.0,<4.0.0',
 'psycopg>=3.0.16,<4.0.0',
 'pymongo>=4.2.0,<5.0.0',
 'rich>=10.14.0,<11.0.0',
 'typer[all]>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['np_data_validator_2 = np_data_validator_2.__main__:app']}

setup_kwargs = {
    'name': 'np-data-validator-2',
    'version': '0.1.9',
    'description': 'Awesome `np_data_validator_2` is a Python cli/package created with https://github.com/TezRomacH/python-package-template',
    'long_description': '# np_data_validator_2\n\n<div align="center">\n\n[![Build status](https://github.com/np_data_validator_2/np_data_validator_2/workflows/build/badge.svg?branch=master&event=push)](https://github.com/np_data_validator_2/np_data_validator_2/actions?query=workflow%3Abuild)\n[![Python Version](https://img.shields.io/pypi/pyversions/np_data_validator_2.svg)](https://pypi.org/project/np_data_validator_2/)\n[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/np_data_validator_2/np_data_validator_2/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)\n[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/np_data_validator_2/np_data_validator_2/blob/master/.pre-commit-config.yaml)\n[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/np_data_validator_2/np_data_validator_2/releases)\n[![License](https://img.shields.io/github/license/np_data_validator_2/np_data_validator_2)](https://github.com/np_data_validator_2/np_data_validator_2/blob/master/LICENSE)\n![Coverage Report](assets/images/coverage.svg)\n\nAwesome `np_data_validator_2` is a Python cli/package created with https://github.com/TezRomacH/python-package-template\n\n</div>\n\n## Very first steps\n\n### Initialize your code\n\n1. Initialize `git` inside your repo:\n\n```bash\ncd np_data_validator_2 && git init\n```\n\n2. If you don\'t have `Poetry` installed run:\n\n```bash\nmake poetry-download\n```\n\n3. Initialize poetry and install `pre-commit` hooks:\n\n```bash\nmake install\nmake pre-commit-install\n```\n\n4. Run the codestyle:\n\n```bash\nmake codestyle\n```\n\n5. Upload initial code to GitHub:\n\n```bash\ngit add .\ngit commit -m ":tada: Initial commit"\ngit branch -M main\ngit remote add origin https://github.com/np_data_validator_2/np_data_validator_2.git\ngit push -u origin main\n```\n\n### Set up bots\n\n- Set up [Dependabot](https://docs.github.com/en/github/administering-a-repository/enabling-and-disabling-version-updates#enabling-github-dependabot-version-updates) to ensure you have the latest dependencies.\n- Set up [Stale bot](https://github.com/apps/stale) for automatic issue closing.\n\n### Poetry\n\nWant to know more about Poetry? Check [its documentation](https://python-poetry.org/docs/).\n\n<details>\n<summary>Details about Poetry</summary>\n<p>\n\nPoetry\'s [commands](https://python-poetry.org/docs/cli/#commands) are very intuitive and easy to learn, like:\n\n- `poetry add numpy@latest`\n- `poetry run pytest`\n- `poetry publish --build`\n\netc\n</p>\n</details>\n\n### Building and releasing your package\n\nBuilding a new version of the application contains steps:\n\n- Bump the version of your package `poetry version <version>`. You can pass the new version explicitly, or a rule such as `major`, `minor`, or `patch`. For more details, refer to the [Semantic Versions](https://semver.org/) standard.\n- Make a commit to `GitHub`.\n- Create a `GitHub release`.\n- And... publish 🙂 `poetry publish --build`\n\n## 🎯 What\'s next\n\nWell, that\'s up to you 💪🏻. I can only recommend the packages and articles that helped me.\n\n- [`Typer`](https://github.com/tiangolo/typer) is great for creating CLI applications.\n- [`Rich`](https://github.com/willmcgugan/rich) makes it easy to add beautiful formatting in the terminal.\n- [`Pydantic`](https://github.com/samuelcolvin/pydantic/) – data validation and settings management using Python type hinting.\n- [`Loguru`](https://github.com/Delgan/loguru) makes logging (stupidly) simple.\n- [`tqdm`](https://github.com/tqdm/tqdm) – fast, extensible progress bar for Python and CLI.\n- [`IceCream`](https://github.com/gruns/icecream) is a little library for sweet and creamy debugging.\n- [`orjson`](https://github.com/ijl/orjson) – ultra fast JSON parsing library.\n- [`Returns`](https://github.com/dry-python/returns) makes you function\'s output meaningful, typed, and safe!\n- [`Hydra`](https://github.com/facebookresearch/hydra) is a framework for elegantly configuring complex applications.\n- [`FastAPI`](https://github.com/tiangolo/fastapi) is a type-driven asynchronous web framework.\n\nArticles:\n\n- [Open Source Guides](https://opensource.guide/).\n- [A handy guide to financial support for open source](https://github.com/nayafia/lemonade-stand)\n- [GitHub Actions Documentation](https://help.github.com/en/actions).\n- Maybe you would like to add [gitmoji](https://gitmoji.carloscuesta.me/) to commit names. This is really funny. 😄\n\n## 🚀 Features\n\n### Development features\n\n- Supports for `Python 3.9` and higher.\n- [`Poetry`](https://python-poetry.org/) as the dependencies manager. See configuration in [`pyproject.toml`](https://github.com/np_data_validator_2/np_data_validator_2/blob/master/pyproject.toml) and [`setup.cfg`](https://github.com/np_data_validator_2/np_data_validator_2/blob/master/setup.cfg).\n- Automatic codestyle with [`black`](https://github.com/psf/black), [`isort`](https://github.com/timothycrosley/isort) and [`pyupgrade`](https://github.com/asottile/pyupgrade).\n- Ready-to-use [`pre-commit`](https://pre-commit.com/) hooks with code-formatting.\n- Type checks with [`mypy`](https://mypy.readthedocs.io); docstring checks with [`darglint`](https://github.com/terrencepreilly/darglint); security checks with [`safety`](https://github.com/pyupio/safety) and [`bandit`](https://github.com/PyCQA/bandit)\n- Testing with [`pytest`](https://docs.pytest.org/en/latest/).\n- Ready-to-use [`.editorconfig`](https://github.com/np_data_validator_2/np_data_validator_2/blob/master/.editorconfig), [`.dockerignore`](https://github.com/np_data_validator_2/np_data_validator_2/blob/master/.dockerignore), and [`.gitignore`](https://github.com/np_data_validator_2/np_data_validator_2/blob/master/.gitignore). You don\'t have to worry about those things.\n\n### Deployment features\n\n- `GitHub` integration: issue and pr templates.\n- `Github Actions` with predefined [build workflow](https://github.com/np_data_validator_2/np_data_validator_2/blob/master/.github/workflows/build.yml) as the default CI/CD.\n- Everything is already set up for security checks, codestyle checks, code formatting, testing, linting, docker builds, etc with [`Makefile`](https://github.com/np_data_validator_2/np_data_validator_2/blob/master/Makefile#L89). More details in [makefile-usage](#makefile-usage).\n- [Dockerfile](https://github.com/np_data_validator_2/np_data_validator_2/blob/master/docker/Dockerfile) for your package.\n- Always up-to-date dependencies with [`@dependabot`](https://dependabot.com/). You will only [enable it](https://docs.github.com/en/github/administering-a-repository/enabling-and-disabling-version-updates#enabling-github-dependabot-version-updates).\n- Automatic drafts of new releases with [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). You may see the list of labels in [`release-drafter.yml`](https://github.com/np_data_validator_2/np_data_validator_2/blob/master/.github/release-drafter.yml). Works perfectly with [Semantic Versions](https://semver.org/) specification.\n\n### Open source community features\n\n- Ready-to-use [Pull Requests templates](https://github.com/np_data_validator_2/np_data_validator_2/blob/master/.github/PULL_REQUEST_TEMPLATE.md) and several [Issue templates](https://github.com/np_data_validator_2/np_data_validator_2/tree/master/.github/ISSUE_TEMPLATE).\n- Files such as: `LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md` are generated automatically.\n- [`Stale bot`](https://github.com/apps/stale) that closes abandoned issues after a period of inactivity. (You will only [need to setup free plan](https://github.com/marketplace/stale)). Configuration is [here](https://github.com/np_data_validator_2/np_data_validator_2/blob/master/.github/.stale.yml).\n- [Semantic Versions](https://semver.org/) specification with [`Release Drafter`](https://github.com/marketplace/actions/release-drafter).\n\n## Installation\n\n```bash\npip install -U np_data_validator_2\n```\n\nor install with `Poetry`\n\n```bash\npoetry add np_data_validator_2\n```\n\nThen you can run\n\n```bash\nnp_data_validator_2 --help\n```\n\nor with `Poetry`:\n\n```bash\npoetry run np_data_validator_2 --help\n```\n\n### Makefile usage\n\n[`Makefile`](https://github.com/np_data_validator_2/np_data_validator_2/blob/master/Makefile) contains a lot of functions for faster development.\n\n<details>\n<summary>1. Download and remove Poetry</summary>\n<p>\n\nTo download and install Poetry run:\n\n```bash\nmake poetry-download\n```\n\nTo uninstall\n\n```bash\nmake poetry-remove\n```\n\n</p>\n</details>\n\n<details>\n<summary>2. Install all dependencies and pre-commit hooks</summary>\n<p>\n\nInstall requirements:\n\n```bash\nmake install\n```\n\nPre-commit hooks coulb be installed after `git init` via\n\n```bash\nmake pre-commit-install\n```\n\n</p>\n</details>\n\n<details>\n<summary>3. Codestyle</summary>\n<p>\n\nAutomatic formatting uses `pyupgrade`, `isort` and `black`.\n\n```bash\nmake codestyle\n\n# or use synonym\nmake formatting\n```\n\nCodestyle checks only, without rewriting files:\n\n```bash\nmake check-codestyle\n```\n\n> Note: `check-codestyle` uses `isort`, `black` and `darglint` library\n\nUpdate all dev libraries to the latest version using one comand\n\n```bash\nmake update-dev-deps\n```\n\n<details>\n<summary>4. Code security</summary>\n<p>\n\n```bash\nmake check-safety\n```\n\nThis command launches `Poetry` integrity checks as well as identifies security issues with `Safety` and `Bandit`.\n\n```bash\nmake check-safety\n```\n\n</p>\n</details>\n\n</p>\n</details>\n\n<details>\n<summary>5. Type checks</summary>\n<p>\n\nRun `mypy` static type checker\n\n```bash\nmake mypy\n```\n\n</p>\n</details>\n\n<details>\n<summary>6. Tests with coverage badges</summary>\n<p>\n\nRun `pytest`\n\n```bash\nmake test\n```\n\n</p>\n</details>\n\n<details>\n<summary>7. All linters</summary>\n<p>\n\nOf course there is a command to ~~rule~~ run all linters in one:\n\n```bash\nmake lint\n```\n\nthe same as:\n\n```bash\nmake test && make check-codestyle && make mypy && make check-safety\n```\n\n</p>\n</details>\n\n<details>\n<summary>8. Docker</summary>\n<p>\n\n```bash\nmake docker-build\n```\n\nwhich is equivalent to:\n\n```bash\nmake docker-build VERSION=latest\n```\n\nRemove docker image with\n\n```bash\nmake docker-remove\n```\n\nMore information [about docker](https://github.com/np_data_validator_2/np_data_validator_2/tree/master/docker).\n\n</p>\n</details>\n\n<details>\n<summary>9. Cleanup</summary>\n<p>\nDelete pycache files\n\n```bash\nmake pycache-remove\n```\n\nRemove package build\n\n```bash\nmake build-remove\n```\n\nDelete .DS_STORE files\n\n```bash\nmake dsstore-remove\n```\n\nRemove .mypycache\n\n```bash\nmake mypycache-remove\n```\n\nOr to remove all above run:\n\n```bash\nmake cleanup\n```\n\n</p>\n</details>\n\n## 📈 Releases\n\nYou can see the list of available releases on the [GitHub Releases](https://github.com/np_data_validator_2/np_data_validator_2/releases) page.\n\nWe follow [Semantic Versions](https://semver.org/) specification.\n\nWe use [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). As pull requests are merged, a draft release is kept up-to-date listing the changes, ready to publish when you’re ready. With the categories option, you can categorize pull requests in release notes using labels.\n\n### List of labels and corresponding titles\n\n|               **Label**               |  **Title in Releases**  |\n| :-----------------------------------: | :---------------------: |\n|       `enhancement`, `feature`        |       🚀 Features       |\n| `bug`, `refactoring`, `bugfix`, `fix` | 🔧 Fixes & Refactoring  |\n|       `build`, `ci`, `testing`        | 📦 Build System & CI/CD |\n|              `breaking`               |   💥 Breaking Changes   |\n|            `documentation`            |    📝 Documentation     |\n|            `dependencies`             | ⬆️ Dependencies updates |\n\nYou can update it in [`release-drafter.yml`](https://github.com/np_data_validator_2/np_data_validator_2/blob/master/.github/release-drafter.yml).\n\nGitHub creates the `bug`, `enhancement`, and `documentation` labels for you. Dependabot creates the `dependencies` label. Create the remaining labels on the Issues tab of your GitHub repository, when you need them.\n\n## 🛡 License\n\n[![License](https://img.shields.io/github/license/np_data_validator_2/np_data_validator_2)](https://github.com/np_data_validator_2/np_data_validator_2/blob/master/LICENSE)\n\nThis project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/np_data_validator_2/np_data_validator_2/blob/master/LICENSE) for more details.\n\n## 📃 Citation\n\n```bibtex\n@misc{np_data_validator_2,\n  author = {np_data_validator_2},\n  title = {Awesome `np_data_validator_2` is a Python cli/package created with https://github.com/TezRomacH/python-package-template},\n  year = {2022},\n  publisher = {GitHub},\n  journal = {GitHub repository},\n  howpublished = {\\url{https://github.com/np_data_validator_2/np_data_validator_2}}\n}\n```\n\n## Credits [![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen)](https://github.com/TezRomacH/python-package-template)\n\nThis project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template)\n',
    'author': 'np_data_validator_2',
    'author_email': 'chrism@alleninstitute.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/np_data_validator_2/np_data_validator_2',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
