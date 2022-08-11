from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name="muckup",
    version='0.1',
    py_modules=['muckup'],
    description="A simple backup utility for folders and files.",
    author="Mano",
    author_email="shapely_indexes0d@icloud.com",
    install_requires=[
        'Click',
    ],
    scripts=['bin/muckup'],
    url="https://github.com/manorajesh/muckup",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Topic :: System :: Archiving :: Backup",
    ],
    keywords="backup utility",
    long_description=readme(),
)