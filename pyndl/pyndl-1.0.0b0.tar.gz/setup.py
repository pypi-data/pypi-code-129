# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyndl']

package_data = \
{'': ['*']}

install_requires = \
['Cython>=0.29.32,<0.30.0',
 'netCDF4>=1.6.0,<2.0.0',
 'numpy>=1.23.1,<2.0.0',
 'pandas>=1.4.3,<2.0.0',
 'scipy>=1.9.0,<2.0.0',
 'xarray>=2022.6.0,<2023.0.0']

setup_kwargs = {
    'name': 'pyndl',
    'version': '1.0.0b0',
    'description': 'Naive discriminative learning implements learning and classification models based on the Rescorla-Wagner equations.',
    'long_description': "===============================================\nPyndl - Naive Discriminative Learning in Python\n===============================================\n\n.. image:: https://github.com/quantling/pyndl/actions/workflows/python-test.yml/badge.svg?branch=master\n    :target: https://github.com/quantling/pyndl/actions/workflows/python-test.yml\n\n.. image:: https://codecov.io/gh/quantling/pyndl/branch/master/graph/badge.svg?token=2GWUXRA9PD\n    :target: https://codecov.io/gh/quantling/pyndl\n\n.. image:: https://img.shields.io/lgtm/grade/python/g/quantling/pyndl.svg?logo=lgtm&logoWidth=18\n    :target: https://lgtm.com/projects/g/quantling/pyndl/context:python\n\n.. image:: https://img.shields.io/pypi/pyversions/pyndl.svg\n    :target: https://pypi.python.org/pypi/pyndl/\n\n.. image:: https://img.shields.io/github/license/quantling/pyndl.svg\n    :target: https://github.com/quantling/pyndl/blob/master/LICENSE.txt\n\n.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.597964.svg\n   :target: https://doi.org/10.5281/zenodo.597964\n\n*pyndl* is an implementation of Naive Discriminative Learning in Python. It was\ncreated to analyse huge amounts of text file corpora. Especially, it allows to\nefficiently apply the Rescorla-Wagner learning rule to these corpora.\n\n\nInstallation\n============\n\nThe easiest way to install *pyndl* is using\n`pip <https://pip.pypa.io/en/stable/>`_:\n\n.. code:: bash\n\n    pip install --user pyndl\n\nFor more information have a look at the `Installation Guide\n<http://pyndl.readthedocs.io/en/latest/installation.html>`_.\n\n\nDocumentation\n=============\n\n*pyndl* uses ``sphinx`` to create a documentation manual. The documentation is\nhosted on `Read the Docs <http://pyndl.readthedocs.io/en/latest/>`_.\n\n\nGetting involved\n================\n\nThe *pyndl* project welcomes help in the following ways:\n\n* Making Pull Requests for\n  `code <https://github.com/quantling/pyndl/tree/master/pyndl>`_,\n  `tests <https://github.com/quantling/pyndl/tree/master/tests>`_\n  or `documentation <https://github.com/quantling/pyndl/tree/master/doc>`_.\n* Commenting on `open issues <https://github.com/quantling/pyndl/issues>`_\n  and `pull requests <https://github.com/quantling/pyndl/pulls>`_.\n* Helping to answer `questions in the issue section\n  <https://github.com/quantling/pyndl/labels/question>`_.\n* Creating feature requests or adding bug reports in the `issue section\n  <https://github.com/quantling/pyndl/issues/new>`_.\n\nFor more information on how to contribute to *pyndl* have a look at the\n`development section <http://pyndl.readthedocs.io/en/latest/development.html>`_.\n\n\nAuthors and Contributers\n========================\n\n*pyndl* was mainly developed by\n`Konstantin Sering <https://github.com/derNarr>`_,\n`Marc Weitz <https://github.com/trybnetic>`_,\n`David-Elias Künstle <https://github.com/dekuenstle/>`_,\n`Elnaz Shafaei Bajestan <https://github.com/elnazsh>`_\nand `Lennart Schneider <https://github.com/sumny>`_. For the full list of\ncontributers have a look at `Github's Contributor summary\n<https://github.com/quantling/pyndl/contributors>`_.\n\nCurrently, it is maintained by `Konstantin Sering <https://github.com/derNarr>`_\nand `Marc Weitz <https://github.com/trybnetic>`_.\n\n\nAcknowledgments\n===============\nThis research was supported by an ERC advanced Grant (no. 742545) and by the\nAlexander von Humboldt Professorship awarded to R. H. Baayen and by the\nUniversity of Tübingen.\n",
    'author': 'Konstantin Sering',
    'author_email': 'konstantin.sering@uni-tuebingen.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pyndl.readthedocs.io/en/latest/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.12',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
