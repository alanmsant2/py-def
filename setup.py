#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.rst") as f:
    readme = f.read()

long_description = readme

setup(
    name="py-def",
    version="v1.0",
    description="A alternative to python -c, run def function",
    long_description=long_description,
    author="Alan MS",
    author_email="alanmsant@gmail.com",
    license="MIT",
    url="https://github.com/alanmsant2/py-def",
    download_url="https://github.com/alanmsant2/py-def/archive/v1.0.tar.gz",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "py-def = py_def.py_def:main",
        ]
    },
)
