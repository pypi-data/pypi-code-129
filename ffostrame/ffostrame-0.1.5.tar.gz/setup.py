from setuptools import setup, find_packages


def read_requirements():
    with open("requirements.txt", "r") as req:
        content = req.read()
        requirements = content.split("\n")

    return requirements


def get_version():
    version_file = open("ff/version.txt", "r")
    version = version_file.read()
    version_file.close()

    return version


setup(
    name="ffostrame",
    version=get_version(),
    author="Fran Nostrame",
    author_email="frank@nostrame.com",
    license="MIT",
    description="A do-it-all Python package for you and me",
    install_requires=read_requirements(),
    python_requires='>=3.6.0',
    package_data={"": ["README.md","LICENSE", "ff/version.txt"]},
    # include_package_data=True,
    packages=find_packages(),
    scripts=[
        "ff/ff.py",
        "ff/version.txt"
    ],
    entry_points="""
        [console_scripts]
        ff=ff:cli
    """,
)
