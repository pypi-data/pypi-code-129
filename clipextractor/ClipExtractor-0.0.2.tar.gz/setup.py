import setuptools
from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ClipExtractor", # Replace with your own username
    version="0.0.2",
    license='MIT',
    author="Falahgs.G.Saleih",
    author_email="falahgs07@gmail.com",
    description="Art Image Captioning Extractor by using CLIP Models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/falahgs/",
    packages=find_packages(),
    keywords = ['Keras', 'Tensorflow', 'Classification'],   # Keywords that define your package best
    install_requires=[ 'ftfy','regex','tqdm','pytorch-lightning','einops','transformers','gitpython','timm==0.4.12','fairscale==0.4.4'],
    classifiers=["Programming Language :: Python :: 3","License :: OSI Approved :: MIT License","Operating System :: OS Independent",],
    python_requires='>=3.6',)