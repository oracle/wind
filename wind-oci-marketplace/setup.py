## Copyright © 2021, Oracle and/or its affiliates. 
## Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.

#!/usr/bin/env python

from setuptools import setup

setup(name='wind-marketplace-library',
      version="1.0.0",
      description='Robot Framework test library for OCI Marketplace',
      long_description='Robot Framework test library for OCI Marketplace',
      classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Framework :: WIND Robot Framework',
      ],
      author='arun.poonia@oracle.com',
      author_email='arun.poonia@oracle.com',
      packages=['MarketplaceLibrary'],
      license = "UPL-1.0",
      install_requires=[
      ],
      extras_require={
          'dev': [
          ]
      },
      platforms='any',
      include_package_data=True,
      zip_safe=False)