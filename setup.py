# coding: utf-8

"""
    finAPI RESTful Services

    finAPI RESTful Services  # noqa: E501

    OpenAPI spec version: v1.67.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "finapi"
VERSION = "0.9.7"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="FinAPI RESTful Services",
    author="mishaker",
    author_email="misagh.shakeri@gmail.com",
    url="",
    keywords=["FinAPI", "FinAPI RESTful Services"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    FinAPI RESTful Services is a python library generated by swagger to consume finapi.io APIs.
    """
)
