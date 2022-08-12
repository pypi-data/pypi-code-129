# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['aioutilities', 'aioutilities.pool']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['aioutilities-example = aioutilities.example:run_example']}

setup_kwargs = {
    'name': 'aioutilities',
    'version': '1.0.3',
    'description': 'asyncio-powered coroutine worker pool',
    'long_description': '# aioutilities\n\n`asyncio`-powered coroutine worker pool. No more juggling bounded semaphores and annoying timeouts, and allows you to run through millions of pieces of data efficiently.\n\n# Installation\n\n```shell\npython -m pip install -U aioutilities\n```\n\n# Credits\n\nThis is refactored and built on top of https://github.com/CaliDog/asyncpool\n\n# Example Usage\n\n```python\nfrom asyncio import Queue, ensure_future, run, sleep\n\nfrom aioutilities.pool import AioPool\n\n\nasync def example_coro(initial_number: int, result_queue: Queue[int]) -> None:\n    result = initial_number * 2\n    print(f"Processing Value! -> {initial_number} * 2 = {result}")\n    await sleep(1)\n    await result_queue.put(initial_number * 2)\n\n\nasync def result_reader(queue: Queue[int | None]) -> None:\n    while True:\n        value = await queue.get()\n        if value is None:\n            break\n        print(f"Got value! -> {value}")\n\n\nasync def example() -> None:\n    result_queue = Queue[int | None]()\n    reader_future = ensure_future(result_reader(result_queue))\n\n    # Start a worker pool with 10 coroutines, invokes `example_coro` and waits for\n    # it to complete or 5 minutes to pass.\n    pool = AioPool[int](\n        name="ExamplePool",\n        task=example_coro,\n        worker_qty=10,\n        timeout=300,\n    )\n    async with pool.spawn() as workers:\n        for i in range(50):\n            await workers.push(i, result_queue)\n\n    await result_queue.put(None)\n    await reader_future\n\n\ndef run_example() -> None:\n    run(example())\n```\n',
    'author': 'Kevin Kirsche',
    'author_email': 'kev.kirsche@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/kkirsche/aioutilities',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4',
}


setup(**setup_kwargs)
