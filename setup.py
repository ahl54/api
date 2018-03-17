from __future__ import absolute_import
import re
import ast
from setuptools import setup

with open('requirements.txt') as f:
    requirements = [l for l in f.read().splitlines() if l]

setup(
    name='etiometry_api',
    description='generates api for QIS tiered data',
    version='1.0',
    author='Anna Lu',
    author_email='anna.lu127@gmail.com',
    packages=['example-app'],
    package_data={},
    include_package_data=False,
    install_requires=requirements,
    tests_require=['pytest'],
    classifiers=[
        'License :: Not for distribution',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
)