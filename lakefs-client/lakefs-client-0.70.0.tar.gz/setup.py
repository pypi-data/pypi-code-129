"""
    lakeFS API

    lakeFS HTTP API  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: services@treeverse.io
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "lakefs-client"
VERSION = "0.70.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="lakeFS API",
    author="Treeverse",
    author_email="services@treeverse.io",
    url="https://github.com/treeverse/lakeFS/tree/master/clients/python",
    keywords=["OpenAPI", "OpenAPI-Generator", "lakeFS API"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    lakeFS HTTP API  # noqa: E501
    """
)
