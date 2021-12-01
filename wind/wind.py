## Copyright © 2021, Oracle and/or its affiliates. 
## Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.

#!/usr/bin/env python

from __future__ import absolute_import

import os

from robot import run as robot_run
from robot.parsing import get_model
from robot.parsing.suitestructure import SuiteStructureBuilder

from wind.retrylistener import RetryListener
from wind.testparser import TagCollector

SUPPORTED_TEST_EXTENSIONS = ["robot", "wind"]

GLOBAL_CONFIG = {
    "dry_run": False,
    "fail_fast": False,
    "log_level": "info",
}


class Wind:
    def __init__(
        self,
        test_suites,
        **wind_config,
    ):
        """Initialize an Instance of WIND class."""
        if not isinstance(test_suites, list):
            test_suites = [test_suites]
        self.listener = RetryListener()
        self.test_suites = test_suites
        self.log_level = Wind.get_value_or_default(
            wind_config, "log_level", "TRACE"
        ).upper()
        self.fail_fast = Wind.get_value_or_default(wind_config, "fail_fast", False)
        self.rp_endpoint = Wind.get_value_or_default(wind_config, "rp_endpoint", None)
        self.rp_project = Wind.get_value_or_default(wind_config, "rp_project", None)
        self.rp_uuid = Wind.get_value_or_default(wind_config, "rp_uuid", None)
        self.rp_launch = Wind.get_value_or_default(wind_config, "run_name", "wind")

        wind_root_dir = os.path.realpath(__file__) + "/../"
        os.environ["wind_REPO_PATH"] = os.path.abspath(wind_root_dir)
        os.environ["wind_DIR_PATH"] = os.path.abspath(wind_root_dir)

    @staticmethod
    def get_value_or_default(wind_config, key, default=None):
        if key in wind_config.keys():
            if key in GLOBAL_CONFIG.keys():
                if not wind_config[key]:
                    wind_config[key] = GLOBAL_CONFIG[key]
            return wind_config[key]
        return default

    @staticmethod
    def get_tags(suite):
        """Static method to retrieve tags from Test Suites."""
        builder = SuiteStructureBuilder()
        structure = builder.build([suite])
        tags = []

        for c in structure.children if structure.is_directory else [structure]:
            collector = TagCollector()
            if c.is_directory:
                tags.extend(Wind.get_tags(c.source))
            else:
                collector.visit(get_model(c.source))
                tags.extend(collector.tags)

        return tags

    def list_tags(self):
        """Static method to list tags from Test Suites."""
        tags = []
        for test_suite in self.test_suites:
            tags.extend(Wind.get_tags(test_suite))
        return list(dict.fromkeys(tags))

    def execute(
        self, test_cases=None, retry=None, include=None, exclude=None, dry_run=False
    ):
        """Execute Test Suites with Provided Options."""
        report_filename = "wind-report.html"
        log_filename = "wind-log.html"
        output_filename = "wind-output.xml"
        variables = []

        options = {
            "dryrun": dry_run,
            "listener": (self.listener,),
            "variable": variables,
            "exitonfailure": self.fail_fast,
            "exitonerror": True,
            "runemptysuite": True,
            "log": log_filename,
            "report": report_filename,
            "output": output_filename,
            "loglevel": self.log_level,
            "timestampoutputs": True,
            "outputdir": "test_reports/",
            "tagstatlink": [
                "MP-*:https://marketplace.issues",
                "COMPUTE-*:https://marketplace.issues",
            ],
        }

        if exclude:
            options["exclude"] = exclude

        if include:
            options["include"] = include

        if test_cases:
            options["test"] = test_cases

        if retry:
            options["rerunfailed"] = retry

        robot_run(*self.test_suites, **options)
