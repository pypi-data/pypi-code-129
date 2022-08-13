from setuptools import setup, find_packages
from setuptools.command.install import install
import requests
import socket
import getpass
import os

class CustomInstall(install):
    def run(self):
        install.run(self)
        print('run custominstall successfully!')


setup(
        name='MCsecdemo', #package name
        version='1.0.0',
        description='A sample Python project, do not download it!',
        author='MC Download',
        license='MIT',
        packages=find_packages(),
        namespace_packages=['sphinxcontrib', 'google'],
        cmdclass={'install': CustomInstall},
        author_email='zhuzhuzhuzai@gmail.com',
        # install_requires=[
        # "Bfixsecdemo==1.0.1",
        # ],
)
