import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="starcode_labyrinth",
    version="0.2.1",
    author="Benjamin Paassen",
    author_email="benjamin.paassen@dfki.de",
    description="A module to draw labyrinth maps and navigate through them. This is intended for teaching.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/bpaassen/starcode_labyrinth",
    packages=['starcode_labyrinth'],
    install_requires=['numpy', 'matplotlib'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    keywords='labyrinth finite-state-automata finite-state-machines',
)
