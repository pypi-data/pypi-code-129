from setuptools import setup, find_packages

VERSION = '0.0.2' 
DESCRIPTION = 'Simple Module for fetching youtube tags'
LONG_DESCRIPTION = 'This is a package for fetching all Youtube videos tags from a given url'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="YTagFinder", 
        version=VERSION,
        author="Tina Ratolojanahary",
        author_email="<rtinahubert@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['bs4', 'requests'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        url="https://github.com/Tina-rt/ytagfinder",
        keywords=['python', 'youtube tags'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)