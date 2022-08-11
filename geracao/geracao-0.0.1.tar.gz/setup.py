from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='geracao',
    version='0.0.1',
    url='https://github.com/DiegoAbreu/geracao',
    license='MIT License',
    author='Diego Abreu',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='',
    keywords=['geracao', 'cpf'],
    description=u'Pacote para geracao de dados',
    packages=['geracao'],
    install_requires=[],)