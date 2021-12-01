## Copyright © 2021, Oracle and/or its affiliates. 
## Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.

#!/usr/bin/env python

from setuptools import setup, find_namespace_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='wind-oracle',
    version='1.0.0',
    description='WIND: Oracle Marketplace Publisher Framework',
    long_description=readme(),
    author='arun.poonia@oracle.com',
    author_email='arun.poonia@oracle.com',
    packages=find_namespace_packages(exclude=['docs']),
    include_package_data=True,
    license = "UPL-1.0",
    entry_points={
        'console_scripts': [
            'wind = wind.cli:cli'
        ]
    },
    install_requires=[
    ],
    extras_require={
        'dev': [
        ]
    }
)
