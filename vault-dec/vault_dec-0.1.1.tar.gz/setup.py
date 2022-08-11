from setuptools import setup, find_packages

version = '0.1.1'

setup(
    name="vault_dec",
    version=version,
    description='Vault Decrypt',
    long_description='Decrypts arbitrary text files (configs, k8s resource specs)'
                     ' by substituting values from HashiCorp Vault',
    author='Aleksey Leontiev',
    author_email='alekseyl@list.ru',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Intended Audience :: Developers',
        'License :: Free for non-commercial use',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[
        'hvac==0.11.*',
        'ConfigArgParse==1.5.*',
    ],
)
