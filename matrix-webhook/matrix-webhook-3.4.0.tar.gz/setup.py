# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['matrix_webhook']

package_data = \
{'': ['*']}

install_requires = \
['Markdown>=3.3.4,<4.0.0', 'matrix-nio>=0.18.3,<0.19.0']

entry_points = \
{'console_scripts': ['matrix-webhook = matrix_webhook.__main__:main']}

setup_kwargs = {
    'name': 'matrix-webhook',
    'version': '3.4.0',
    'description': 'Post a message to a matrix room with a simple HTTP POST',
    'long_description': '# Matrix Webhook\n\n[![Tests](https://github.com/nim65s/matrix-webhook/actions/workflows/test.yml/badge.svg)](https://github.com/nim65s/matrix-webhook/actions/workflows/test.yml)\n[![Lints](https://github.com/nim65s/matrix-webhook/actions/workflows/lint.yml/badge.svg)](https://github.com/nim65s/matrix-webhook/actions/workflows/lint.yml)\n[![Docker-Hub](https://github.com/nim65s/matrix-webhook/actions/workflows/docker-hub.yml/badge.svg)](https://hub.docker.com/r/nim65s/matrix-webhook)\n[![Release](https://github.com/nim65s/matrix-webhook/actions/workflows/release.yml/badge.svg)](https://pypi.org/project/matrix-webhook/)\n[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/nim65s/matrix-webhook/master.svg)](https://results.pre-commit.ci/latest/github/nim65s/matrix-webhook/main)\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![codecov](https://codecov.io/gh/nim65s/matrix-webhook/branch/master/graph/badge.svg?token=BLGISGCYKG)](https://codecov.io/gh/nim65s/matrix-webhook)\n[![Maintainability](https://api.codeclimate.com/v1/badges/a0783da8c0461fe95eaf/maintainability)](https://codeclimate.com/github/nim65s/matrix-webhook/maintainability)\n[![PyPI version](https://badge.fury.io/py/matrix-webhook.svg)](https://badge.fury.io/py/matrix-webhook)\n\nPost a message to a matrix room with a simple HTTP POST\n\n## Install\n\n```\npython3 -m pip install matrix-webhook\n# OR\ndocker pull nim65s/matrix-webhook\n```\n\n## Start\n\nCreate a matrix user for the bot, and launch this app with the following arguments and/or environment variables\n(environment variables update defaults, arguments take precedence):\n\n```\nmatrix-webhook -h\n# OR\npython -m matrix_webhook -h\n# OR\ndocker run --rm -it nim65s/matrix-webhook -h\n```\n\n```\nusage: python -m matrix_webhook [-h] [-H HOST] [-P PORT] [-u MATRIX_URL] -i MATRIX_ID -p MATRIX_PW -k API_KEY [-v]\n\nConfiguration for Matrix Webhook.\n\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -H HOST, --host HOST  host to listen to. Default: `\'\'`. Environment variable: `HOST`\n  -P PORT, --port PORT  port to listed to. Default: 4785. Environment variable: `PORT`\n  -u MATRIX_URL, --matrix-url MATRIX_URL\n                        matrix homeserver url. Default: `https://matrix.org`. Environment variable: `MATRIX_URL`\n  -i MATRIX_ID, --matrix-id MATRIX_ID\n                        matrix user-id. Required. Environment variable: `MATRIX_ID`\n  -p MATRIX_PW, --matrix-pw MATRIX_PW\n                        matrix password. Required. Environment variable: `MATRIX_PW`\n  -k API_KEY, --api-key API_KEY\n                        shared secret to use this service. Required. Environment variable: `API_KEY`\n  -v, --verbose         increment verbosity level\n```\n\n\n## Dev\n\n```\npoetry install\n# or python3 -m pip install --user markdown matrix-nio\npython3 -m matrix_webhook\n```\n\n## Prod\n\nA `docker-compose.yml` is provided:\n\n- Use [Traefik](https://traefik.io/) on the `web` docker network, eg. with\n  [proxyta.net](https://framagit.org/oxyta.net/proxyta.net)\n- Put the configuration into a `.env` file\n- Configure your DNS for `${CHATONS_SERVICE:-matrixwebhook}.${CHATONS_DOMAIN:-localhost}`\n\n```\ndocker-compose up -d\n```\n\n## Test / Usage\n\n```\ncurl -d \'{"body":"new contrib from toto: [44](http://radio.localhost/map/#44)", "key": "secret"}\' \\\n  \'http://matrixwebhook.localhost/!DPrUlnwOhBEfYwsDLh:matrix.org\'\n```\n(or localhost:4785 without docker)\n\n### For Github\n\nAdd a JSON webhook with `?formatter=github`, and put the `API_KEY` as secret\n\n### For Grafana\n\nAdd a webhook with an URL ending with `?formatter=grafana&key=API_KEY`\n\n### For Gitlab\n\nAt a group level, Gitlab does not permit to setup webhooks. A workaround consists to use Google\nChat or Microsoft Teams notification integration with a custom URL (Gitlab does not check if the url begins with the normal url of the service).\n\n#### Google Chat\n\nAdd a Google Chat integration with an URL ending with `?formatter=gitlab_gchat&key=API_KEY`\n\n#### Microsoft Teams\n\nAdd a Microsoft Teams integration with an URL ending with `?formatter=gitlab_teams&key=API_KEY`\n\n## Test room\n\n[#matrix-webhook:tetaneutral.net](https://matrix.to/#/!DPrUlnwOhBEfYwsDLh:matrix.org)\n\n## Unit tests\n\n```\ndocker-compose -f test.yml up --exit-code-from tests --force-recreate --build\n```\n',
    'author': 'Guilhem Saurel',
    'author_email': 'guilhem.saurel@laas.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/nim65s/matrix-webhook',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
