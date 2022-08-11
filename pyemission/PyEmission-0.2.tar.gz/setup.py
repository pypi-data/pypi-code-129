import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="PyEmission",
    packages=["PyEmission"],
    version="0.2",
    description="PyEmission is a Python library for the estimation of gasoline vehicular emissions and fuel consumption",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/IdahoLabResearch/PyEmission",
    author="Md Mamunur Rahman; Ruby Nguyen",
    author_email="mdmamunur.rahman@inl.gov",
    license="Apache-2.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=["numpy", "pandas", "matplotlib"],

)