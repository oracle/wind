## Copyright © 2021, Oracle and/or its affiliates. 
## Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.

from .marketplace import Marketplace


class MarketplaceLibrary(Marketplace):
    def __init__(self):
        for base in MarketplaceLibrary.__bases__:
            base.__init__(self)
