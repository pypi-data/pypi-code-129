#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['tuxsuite', 'tuxsuite.cli']

package_data = \
{'': ['*']}

install_requires = \
['attrs', 'Click', 'requests', 'pyyaml', 'voluptuous', 'b4']

entry_points = \
{'console_scripts': ['tuxsuite = tuxsuite.cli:main']}

setup(name='tuxsuite',
      version='0.49.0',
      description='This is the tuxsuite module.',
      author='Senthil Kumaran',
      author_email='senthil.kumaran@linaro.org',
      url='https://www.tuxsuite.com/',
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      entry_points=entry_points,
      python_requires='>=3.6',
     )
