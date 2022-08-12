import os
import sys

from densefog.server import create_api
from densefog import config

import pytest



@pytest.fixture
def api():
    config.setup().apply(**{
        'app_root': os.path.dirname(os.path.abspath(__file__)),
        'log_dir': '/tmp/densefog.log'
    })

    api = create_api('public', debug=True)
    api.route({
        'ActionName': lambda x: {'text': 'hello world'},
    })

    # no need to start listening.
    # api.start(port=8080)
    return api;


class Test:
    def test_base(self, api):
        result = api.service.app.test_client().get('/')
        assert 200 == result.status_code

        result = api.service.app.test_client().post('/')
        assert 200 == result.status_code
