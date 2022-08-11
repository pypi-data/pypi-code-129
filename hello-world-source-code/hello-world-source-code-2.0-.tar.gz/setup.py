import hello_world_source_code,os
from setuptools import setup

# Change to the directory of setup.py
try:os.chdir(os.path.split(__file__)[0])
except:raise

setup(
  name='hello-world-source-code',
  version=hello_world_source_code.__version__,
  description=hello_world_source_code.__doc__,
  author="Warren Sande and Carter Sande",
  packages=['hello_world_source_code'],
  keywords=["hello-world","source","code"],
  classifiers=[
      'Programming Language :: Python',
      'Programming Language :: Python :: 2',],
  install_requires=["easygui","pygame"]
)
