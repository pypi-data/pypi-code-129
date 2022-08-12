from setuptools import find_packages, setup


with open("README.md", "r") as fh:
	description = fh.read()

setup(
    name='predict-the-object-collision',
    packages=["predict_collision"],
    version='0.2.0',
    description='The goal of this project is to predict the collision of nearest objects around the mighty EARTH.',
    long_description=description,
    long_description_content_type="text/markdown",
    author='Sultan Mahmud Nahian',
    author_email="sultanmahmud621@gmail.com",
    url="https://github.com/smn06/Predict-the-Collision-and-Save-the-Earth",
    license='MIT',
)

