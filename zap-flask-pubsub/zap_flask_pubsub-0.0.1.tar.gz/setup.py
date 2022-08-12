import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zap_flask_pubsub",                     # This is the name of the package
    version="0.0.1",                        # The initial release version
    author="Naresh Kumar",                     # Full name of the author
    description="Subscribe and Publish data through broker message queue",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    keywords=["flask", "pubsub", "RabbitMQ"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=["zap_flask_pubsub"],             # Name of the python package
    # package_dir={'':''},     # Directory of the source code of the package
    install_requires=['pika<=1.3.0']                     # Install other dependencies if any
)
