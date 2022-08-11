from setuptools import setup

setup(
    name='ghviztoggle',
    version='1.0.0',
    description='Quickly toggle the visibility of your GitHub repositories.',
    url='https://github.com/CakeCrusher/ghviztoggle',
    author='Sebastian Sosa',
    author_email='1sebastian1sosa1@gmail.com',
    packages=['ghviztoggle'],
    install_requires=[
        'requests',
        'typer',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.10',
    ],
)