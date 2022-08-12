# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stweet',
 'stweet.auth',
 'stweet.auth.fail_strategy',
 'stweet.exceptions',
 'stweet.get_user_runner',
 'stweet.http_request',
 'stweet.http_request.interceptor',
 'stweet.http_request.requests',
 'stweet.model',
 'stweet.raw_output',
 'stweet.search_runner',
 'stweet.tweets_by_ids_runner',
 'stweet.twitter_api']

package_data = \
{'': ['*']}

install_requires = \
['arrow>=1.2.0,<2.0.0',
 'pandas>=1.3.3,<2.0.0',
 'requests>=2.26.0,<3.0.0',
 'tor-python-easy>=0.1.2,<0.2.0']

setup_kwargs = {
    'name': 'stweet',
    'version': '2.0.1',
    'description': 'Package to scrap tweets',
    'long_description': "# stweet\n\n[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)\n![Python package](https://github.com/markowanga/stweet/workflows/Python%20package/badge.svg?branch=master)\n[![PyPI version](https://badge.fury.io/py/stweet.svg)](https://badge.fury.io/py/stweet)\n[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)\n\nA modern fast python library to scrap tweets and users quickly from Twitter unofficial API.\n\nThis tool helps you to scrap tweets by a search phrase, tweets by ids and user by usernames. It uses\nthe Twitter API, the same API is used on a website.\n\n## Inspiration for the creation of the library\n\nI have used twint to scrap tweets, but it has many errors, and it doesn't work properly. The code\nwas not simple to understand. All tasks have one config, and the user has to know the exact\nparameter. The last important thing is the fact that Api can change — Twitter is the API owner and\nchanges depend on it. It is annoying when something does not work and users must report bugs as\nissues.\n\n## Main advantages of the library\n\n- **Simple code** — the code is not only mine, every user can contribute to the library\n- **Domain objects and interfaces** — the main part of functionalities can be replaced (eg. calling\n  web requests), the library has basic simple solution — if you want to expand it, you can do it\n  without any problems and forks\n- ~~**100% coverage with integration tests** — this advantage can find the API changes, tests are\n  carried out every week and when the task fails, we can find the source of change easily~~ – not in\n  version 2.0\n- **Custom tweets and users output** — it is a part of the interface, if you want to save tweets and\n  users custom format, it takes you a brief moment\n\n## Installation\n\n```shell script\npip install -U stweet\n```\n\n## Donate\n\nIf you want to sponsor me, in thanks for the project, please send me some crypto 😁:\n\n|Coin|Wallet address|\n|---|---|\n|Bitcoin|3EajE9DbLvEmBHLRzjDfG86LyZB4jzsZyg|\n|Etherum|0xE43d8C2c7a9af286bc2fc0568e2812151AF9b1FD|\n\n## Basic usage\n\nTo make a simple request the scrap **task** must be prepared. The task should be processed by **\nrunner**.\n\n```python\nimport stweet as st\n\n\ndef try_search():\n    search_tweets_task = st.SearchTweetsTask(all_words='#covid19')\n    output_jl_tweets = st.JsonLineFileRawOutput('output_raw_search_tweets.jl')\n    output_jl_users = st.JsonLineFileRawOutput('output_raw_search_users.jl')\n    output_print = st.PrintRawOutput()\n    st.TweetSearchRunner(search_tweets_task=search_tweets_task,\n                         tweet_raw_data_outputs=[output_print, output_jl_tweets],\n                         user_raw_data_outputs=[output_print, output_jl_users]).run()\n\n\ndef try_user_scrap():\n    user_task = st.GetUsersTask(['iga_swiatek'])\n    output_json = st.JsonLineFileRawOutput('output_raw_user.jl')\n    output_print = st.PrintRawOutput()\n    st.GetUsersRunner(get_user_task=user_task, raw_data_outputs=[output_print, output_json]).run()\n\n\ndef try_tweet_by_id_scrap():\n    id_task = st.TweetsByIdTask('1447348840164564994')\n    output_json = st.JsonLineFileRawOutput('output_raw_id.jl')\n    output_print = st.PrintRawOutput()\n    st.TweetsByIdRunner(tweets_by_id_task=id_task,\n                        raw_data_outputs=[output_print, output_json]).run()\n\n\nif __name__ == '__main__':\n    try_search()\n    try_user_scrap()\n    try_tweet_by_id_scrap()\n```\n\nExample above shows that it is few lines of code required to scrap tweets.\n\n## Export format\n\nStweet uses api from website so there is no documentation about receiving response. Response is\nsaving as raw so final user must parse it on his own. Maybe parser will be added in feature.\n\nScrapped data can be exported in different ways by using `RawDataOutput` abstract class. List of\nthese outputs can be passed in every runner – yes it is possible to export in two different ways.\n\nCurrently, stweet have implemented:\n\n- **CollectorRawOutput** – can save data in memory and return as list of objects\n- **JsonLineFileRawOutput** – can export data as json lines\n- **PrintEveryNRawOutput** – prints every N-th item\n- **PrintFirstInBatchRawOutput** – prints first item in batch\n- **PrintRawOutput** – prints all items (not recommended in large scrapping)\n\n## Using tor proxy\nLibrary is integrated with [tor-python-easy](https://github.com/markowanga/tor-python-easy).\nIt allows using tor proxy with exposed control port – to change ip when it is needed.\n\nIf you want to use tor proxy client you need to prepare custom web client and use it in runner.\n\nYou need to run tor proxy -- you can run it on your local OS, or you can use this \n[docker-compose](https://github.com/markowanga/tor-python-easy/blob/main/docker-compose.yml).\n\nCode snippet below show how to use proxy:\n```python\nimport stweet as st\n\nif __name__ == '__main__':\n    web_client = st.DefaultTwitterWebClientProvider.get_web_client_preconfigured_for_tor_proxy(\n        socks_proxy_url='socks5://localhost:9050',\n        control_host='localhost',\n        control_port=9051,\n        control_password='test1234'\n    )\n\n    search_tweets_task = st.SearchTweetsTask(all_words='#covid19')\n    output_jl_tweets = st.JsonLineFileRawOutput('output_raw_search_tweets.jl')\n    output_jl_users = st.JsonLineFileRawOutput('output_raw_search_users.jl')\n    output_print = st.PrintRawOutput()\n    st.TweetSearchRunner(search_tweets_task=search_tweets_task,\n                         tweet_raw_data_outputs=[output_print, output_jl_tweets],\n                         user_raw_data_outputs=[output_print, output_jl_users],\n                         web_client=web_client).run()\n```\n\n## Twint inspiration\n\nSmall part of library uses code from [twint](https://github.com/twintproject/twint). Twint was also\nmain inspiration to create stweet.\n",
    'author': 'Marcin Wątroba',
    'author_email': 'markowanga@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
