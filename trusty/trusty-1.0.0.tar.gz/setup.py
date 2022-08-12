import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='trusty',
    version='1.0.0',
    author='Chris Varga',
    author_email='',
    description='Persistent dictionary',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python',
        "Operating System :: OS Independent",
    ],
    install_requires=[
    ],
    keywords="trusty dictionary json persistent",
)
