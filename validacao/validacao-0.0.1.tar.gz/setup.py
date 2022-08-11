from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='validacao',
    version='0.0.1',
    url='https://github.com/DiegoAbreu/validacao',
    license='MIT License',
    author='Diego Abreu',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='',
    keywords=['validacao', 'cpf'],
    description=u'Pacote para validações',
    packages=['validacao'],
    install_requires=[],)