import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='nnhammer',
    version='1.0.2',
    author='Dai Jian',
    author_email='daijian@stumail.ysu.edu.cn',
    description='My hammer.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='~=3.7',
    install_requires=[
        'numpy >= 1.21.0',
        'nibabel >= 4.0.1',
        'scipy >= 1.7.3',
        'medpy >= 0.4.0'
    ]
)
