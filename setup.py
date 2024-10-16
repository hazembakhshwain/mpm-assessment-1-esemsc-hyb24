"""
Setup configuration for the acsefunctions package.

This module uses setuptools to configure the installation of the package, 
including its dependencies and metadata.
"""

from setuptools import setup, find_packages

setup(
    name="acsefunctions",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",  "scipy"
    ],
)
