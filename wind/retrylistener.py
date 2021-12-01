## Copyright © 2021, Oracle and/or its affiliates. 
## Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.

class RetryListener:

    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self):
        """Initialize an Instance of Custom Listner class.
        """
        self.succeeded = True
        self.name = None

    def end_test(self, name, attrs):
        """Check if a Test Case Passed or Failed.
        """
        self.name = name
        self.succeeded = attrs["status"] != "FAIL"

    def end_suite(self, name, attrs):
        """Check if a Test Suite Passed or Failed.
        """
        self.name = name
        self.succeeded = attrs["status"] != "FAIL"

    def output_file(self, path):
        """Display an error if test case/suite failed.
        """
        if not self.succeeded:
            print(
                "> WIND ERROR :: Some test cases have failed, to retry, use flag: --retry {} in your WIND command line.".format(
                    path
                )
            )
