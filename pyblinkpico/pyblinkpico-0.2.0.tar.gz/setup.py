from setuptools import setup

with open("README.md", "r") as fp:
    long_description = fp.read()

setup(
    name='pyblinkpico',
    version='0.2.0',
    description='The BlinkPico shield library to be used with RPI Pico',
    url='https://github.com/ID220/BlinkPico',
    author='Andrea Bianchi',
    author_email='andrea@kaist.ac.kr',
    license='MIT',
    packages=['pyblinkpico'],
    keywords=['education', 'matrix_shield', 'HT16K33', 'RPI Pico'],
    install_requires=[],
    long_description=long_description,
    long_description_content_type="text/markdown",

    classifiers=[
        'Intended Audience :: Education',
        'Programming Language :: Python :: Implementation :: MicroPython'
    ],
)
