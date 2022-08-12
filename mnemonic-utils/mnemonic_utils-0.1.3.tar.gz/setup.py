from setuptools import setup, find_packages
import mnemonic_utils

with open("README.md", "r") as f:
    description = f.read()

setup(
    name="mnemonic_utils",
    version=mnemonic_utils.__version__,
    author="Wira Dharma Kencana Putra",
    author_email="wiradharma_kencanaputra@yahoo.com",
    description="mnemonic_utils is a small library to ease mnemonic and address generation",
    long_description=description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    install_requires=['web3'],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Natural Language :: English"
    ],
    keywords="mnemonic web3 blokchain address",
    url="https://github.com/WiraDKP/mnemonic_utils"
)
