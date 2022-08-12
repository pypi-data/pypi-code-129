from setuptools import setup, find_packages

setup(
  name="testware",
  version="1",
  author="dylan",
  author_email="d@doop.fun",
  description="Malicious Python Module Experimentation",
  long_description=open("README.md").read(),
  long_description_content_type="text/markdown",
  url="https://github.com/pastewow/testware",
  project_urls={
    "GitHub": "https://github.com/pastewow/testware",
  },
  license="MIT",
  keywords=["malware"],
  classifiers = [
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: Microsoft :: Windows",
  "Development Status :: 5 - Production/Stable",
  "Intended Audience :: Developers",
  "Natural Language :: English",
  "Topic :: Software Development"
  ],
  package_dir={"": "."},
  packages=find_packages(where="."),
  install_requires=['requests']
)
