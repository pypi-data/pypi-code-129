import PyWireframe,os
from setuptools import setup

try:os.chdir(os.path.split(__file__)[0])
except:pass

desc="This is an extended version of package PyWireframe. Some bugs from the old version have been fixed."

try:
    long_desc=open("README.rst").read()
except OSError:
    long_desc=desc

setup(
  name='PyWireframe-extended',
  version=PyWireframe.__version__,
  description=desc,
  long_description=long_desc,
  author="Uploader: 七分诚意",
  url="https://pypi.org/project/PyWireframe-extended/",
  packages=['PyWireframe'],
  keywords=["pywireframe","turtle","3d","graphics","绘图"],
  classifiers=[
      "Programming Language :: Python :: 3",
      "Operating System :: OS Independent",
      "Topic :: Education"],
)
