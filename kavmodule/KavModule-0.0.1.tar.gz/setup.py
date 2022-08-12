import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="KavModule",
    version="0.0.1",
    author="Kavish Arora",
    description="A library that can do basic high school science, english, and math.",
    python_requires='>=3.6'
)
