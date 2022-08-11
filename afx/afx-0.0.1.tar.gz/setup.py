#!/usr/bin/env python3.8
from setuptools import setup


description = "Implements the Terraform Registry API in AWS Lambda"

setup(
    name="afx",
    version="0.0.1",
    description=description,
    long_description=description,
    install_requires=[
        "boto3",
        "fastapi",
        "mangum",
        "dynamojo",
        "mypy_boto3_dynamodb",
        "semantic_version"
    ],
    package_dir={
        "afx": "afx",
    },
    packages=["afx"],
    include_package_data=True,
    setup_requires=["setuptools"]
)
