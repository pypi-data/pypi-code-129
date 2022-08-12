import setuptools, platform

with open('README.md') as f:
    long_description = f.read()

if platform.system() == "Darwin":
    req_list = ["appscript==1.2.0", "beautifulsoup4==4.11.1", "requests==2.27.1"]
else:
    req_list = ["beautifulsoup4==4.11.1", "requests==2.27.1"]

setuptools.setup(
    name='n4s',
    version='2.3.0',
    author='Mike Afshari',
    author_email='theneed4swede@gmail.com',
    description='Collection of useful methods by Need4Swede',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/n4s/n4s',
    license='MIT',
    install_requires=req_list,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)