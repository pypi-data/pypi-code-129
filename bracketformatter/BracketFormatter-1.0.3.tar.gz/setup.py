import setuptools

setuptools.setup(
        name="BracketFormatter",
        author="AJ Poulter",
        author_email='ajp@auctoris.co.uk',
        url='https://gitlab.com/Auctoris/bracketformatter',
        version="1.0.3",
        readme="README.md",
        license="LICENSE",
        description="A custom logging formatter to use a [+] style log comment",
        long_description="A custom log formatter class for use with a streaming log handler to print logging messages using a [+] type symbol to denote the severity.",
        packages=["BracketFormatter"])
