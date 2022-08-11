# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['perun', 'perun.backend']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'click>=8.1.3,<9.0.0',
 'h5py>=3.7.0,<4.0.0',
 'mpi4py>=3.1.3,<4.0.0',
 'py-cpuinfo>=8.0.0,<9.0.0',
 'pyRAPL>=0.2.3,<0.3.0',
 'pynvml>=11.4.1,<12.0.0',
 'python-dotenv>=0.20.0,<0.21.0']

entry_points = \
{'console_scripts': ['perun = perun.cli:cli']}

setup_kwargs = {
    'name': 'perun',
    'version': '0.1.0b5',
    'description': '',
    'long_description': '<div align="center">\n  <img src="https://raw.githubusercontent.com/Helmholtz-AI-Energy/perun/main/doc/images/perun.svg">\n</div>\n\nHave you ever wondered how much energy is used when training your neural network on the MNIST dataset? Want to get scared because of impact you are having on the evironment while doing "valuable" research? Are you interested in knowing how much carbon you are burning playing with DALL-E just to get attention on twitter? If the thing that was missing from your machine learning workflow was existential dread, this is the correct package for you!\n\n## Installation\n\nFrom PyPI:\n\n```$ pip install perun```\n\nFrom Github:\n\n```$ pip install git+https://github.com/Helmholtz-AI-Energy/perun```\n\n### Parallel h5py\n\nTo build h5py with mpi support:\n\n```CC=mpicc HDF5_MPI="ON" pip install --no-binary h5py h5py```\n\n## Usage\n\n### Command line\n\nTo get a quick report of the power usage of a python script simply run\n\n```$ perun monitor --format yaml path/to/your/script.py [args]```\n\nOr\n\n```$ python -m perun monitor --format json -o results/ path/to/your/script.py [args]```\n\n### Decorator\n\nOr decorate the function that you want analysed\n\n```python\nimport perun\n\n@perun.monitor(outDir="results/", format="txt")\ndef training_loop(args, model, device, train_loader, test_loader, optimizer, scheduler):\n    for epoch in range(1, args.epochs + 1):\n        train(args, model, device, train_loader, optimizer, epoch)\n        test(model, device, test_loader)\n        scheduler.step()\n\n```\n',
    'author': 'Gutiérrez Hermosillo Muriedas, Juan Pedro',
    'author_email': 'juanpedroghm@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Helmholtz-AI-Energy/perun',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
