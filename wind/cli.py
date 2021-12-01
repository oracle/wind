## Copyright © 2021, Oracle and/or its affiliates. 
## Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.

#!/usr/bin/env python
from __future__ import absolute_import

import sys

import click
import confuse

from wind import wind

CONTEXT_SETTINGS = dict(auto_envvar_prefix="WIND")


def get_value_or_default(config, key, default=None):
    if config[key].exists():
        return config[key].get()
    return default


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option(
    "--dry-run",
    "dry_run",
    is_flag=True,
    help="Verifies test data and runs tests without executing keywords",
    show_envvar=True,
)
@click.option(
    "--fail-fast",
    "fail_fast",
    is_flag=True,
    help="Test will fail fast on any failure",
    show_envvar=True,
)
@click.option(
    "--log-level",
    "log_level",
    type=click.Choice(
        ["error", "warn", "info", "debug", "trace", "none"], case_sensitive=False
    ),
    help="General log level, default info",
    show_envvar=True,
)
@click.option(
    "--list-tags",
    "list_tags",
    is_flag=True,
    help="List all available tags.",
)
@click.option(
    "--include-tag",
    "include_tag",
    multiple=True,
    help="Run test cases with provided tag. Example: tag1",
    show_envvar=True,
)
@click.option(
    "--exclude-tag",
    "exclude_tag",
    multiple=True,
    help="Exclude test cases with provided tag. Example: tag2",
    show_envvar=True,
)
@click.option(
    "--config",
    "-c",
    "config_file",
    help="WIND config YAML File.",
    show_envvar=True,
)
@click.option(
    "--test-case",
    "test_cases",
    multiple=True,
    help="Run a particular test case",
    show_envvar=True,
)
@click.option(
    "--retry",
    "retry",
    help="Retry failed tests using generated xml file.",
    show_envvar=True,
)
@click.argument("test_suites", nargs=-1)
@click.version_option()
@click.help_option("--help", "-h")
def cli(test_suites, **wind_config):
    """Execute WIND Test Suite"""
    config = confuse.Configuration("wind", read=True)
    # Look for configuration in local working directory
    try:
        config.set_file("./config.yaml")
    except confuse.ConfigReadError:
        pass

    if wind_config["config_file"]:
        try:
            config.set_file(wind_config["config_file"])
        except confuse.ConfigReadError as error:
            print(error)
            sys.exit(1)

    config.set_args(wind_config)
    for key, value in wind_config.items():
        if key in wind.GLOBAL_CONFIG.keys():
            if not value:
                value = wind.GLOBAL_CONFIG[key]
        wind_config[key] = get_value_or_default(config, key, value)

    try:
        wind_runner = wind.Wind(
            list(test_suites),
            **wind_config,
        )
    except Exception as error:  # pylint: disable=broad-except
        print(error)
        sys.exit(1)

    if wind_config["list_tags"]:
        print(wind_runner.list_tags())
        sys.exit(0)

    wind_runner.execute(
        test_cases=wind_config["test_cases"],
        retry=wind_config["retry"],
        include=wind_config["include_tag"],
        exclude=wind_config["exclude_tag"],
        dry_run=wind_config["dry_run"],
    )
