from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.1'
DESCRIPTION = 'A package that allows to calculate differents Weight Matrix'

# Setting up
setup(
    name="Weight_Matrix",
    version=VERSION,
    author="Nathanael Duque",
    author_email="<nathanael.duque.gadelha@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy'],
    keywords=['python', 'distributed', 'consensus', 'diffusion', 'exact diffusion', 'agents'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)