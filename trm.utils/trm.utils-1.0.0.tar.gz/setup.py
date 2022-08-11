from setuptools import setup

# Read files used for the long description
with open('README.rst') as f:
    readme = f.read()

#with open('HISTORY.rst') as f:
#    history = f.read()

setup(
    name='trm.utils',
    version='1.0.0',
    packages = ['trm.utils',],

    # metadata
    author='Tom Marsh',
    author_email='t.r.marsh@warwick.ac.uk',
    description="Allows scripts to remember parameter input values",
#    long_description=readme + '\n\n' + history,
    long_description=readme,
    long_description_content_type='text/xrst',
    url='https://github.com/trmrsh/trm-utils',

    # Choose your license
    license='BSD',

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Astronomy',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: BSD License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    install_requires=['astropy','numpy','scipy'],

    # Makes significant use of fstrings which only came in python v3.6
    python_requires='>=3.6',

)

