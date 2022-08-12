from setuptools import setup, find_packages


setup(
    name="reformer-cil",
    version="1.0",
    description="Сonversion of Cyrillic into Latin",
    long_description=open("pypi_description.txt").read(),
    url="https://github.com/bullbesh/reformer",
    author="bullbesh",
    author_email="babulehaha@gmail.com",
    license="MIT",
    packages=find_packages(),
)
