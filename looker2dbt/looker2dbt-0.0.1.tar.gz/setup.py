"""
pypi setup
"""
import os
from setuptools import setup

from version import __version__

_here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(_here, 'DESCRIPTION.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(os.path.join(_here, 'requirements.txt'), encoding='utf-8') as f:
    req_lines = f.read()
    requirements = req_lines.splitlines()

setup(
    name='looker2dbt',
    version=__version__,
    description='A package to translate lookml to dbt yaml.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Rasgo Intelligence',
    author_email='patrick@rasgoml.com',
    project_urls={
        'Source': 'https://github.com/rasgointelligence/looker2dbt',
        'Changelog': 'https://github.com/rasgointelligence/looker2dbt/blob/main/CHANGELOG.md',
        'Rasgo': 'https://www.rasgoml.com/',  
    },
    license='GNU Affero General Public License v3 or later (AGPLv3+)',
    packages=[
        'main',
    ],
    install_requires=requirements,
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Database',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Code Generators',
    ],
)
