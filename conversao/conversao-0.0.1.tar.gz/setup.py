from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='conversao',
    version='0.0.1',
    url='https://github.com/DiegoAbreu/Conversao',
    license='MIT License',
    author='Diego Abreu',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='',
    keywords=['conversao', 'medidas'],
    description=u'Pacote para conversões',
    packages=['conversao'],
    install_requires=[],)