# WIND

`WIND` is a Python library and CLI tool which gives an easy to use and full featured test framework for OCI [Marketplace Publisher Portal APIs](https://docs.oracle.com/en/cloud/marketplace/partner-portal/rest-api-publisher/index.html).

## Installation

You should complete below pre-requisites before proceeding to installation:

- Your organization should be signed up as Marketplace Publisher. If not already signed up, see How do I become a [Marketplace Publisher](https://docs.oracle.com/en/cloud/marketplace/partner-portal/partp/how-do-i-become-marketplace-publisher.html) ? 
- Request an oAuth client ID, Secret Key & API URL from the Marketplace Administrator; email to: marketplace-help_us_grp@oracle.com
- Make sure **python3** installed locally or in your Environment where you will be running this Tool.

To build `WIND` from git (master branch), run below commands:

```bash
git clone https://github.com/oracle/wind.git
pip3 install -r requirements.txt
pip3 install .
cd wind-oci-marketplace
pip3 install . 
cd .. 
```

## Documentation

OCI Marketplace library exposes Publisher APIs to consume partner portal and perform required `CRUD` operations. This Library includes below keywords. You can know more about how to use them using below table: 

- Explore **Keywords** to know more about how to use them [here](./docs/README.md)

## Examples

The easiest way to interact with `WIND` is through the CLI. When in doubt, use the `--help` or `-h` option to display the command's help message.

```shell
user@machine:~$ wind --help     
Usage: wind [OPTIONS] [TEST_SUITES]...

  Execute WIND Test Suite

Options:
  --dry-run                       Verifies test data and runs tests without
                                  executing keywords  [env var: WIND_DRY_RUN]
  --fail-fast                     Test will fail fast on any failure  [env
                                  var: WIND_FAIL_FAST]
  --log-level [error|warn|info|debug|trace|none]
                                  General log level, default info  [env var:
                                  WIND_LOG_LEVEL]
  --list-tags                     List all available tags.
  --include-tag TEXT              Run test cases with provided tag. Example:
                                  tag1  [env var: WIND_INCLUDE_TAG]
  --exclude-tag TEXT              Exclude test cases with provided tag.
                                  Example: tag2  [env var: WIND_EXCLUDE_TAG]
  -c, --config TEXT               WIND config YAML File.  [env var:
                                  WIND_CONFIG_FILE]
  --test-case TEXT                Run a particular test case  [env var:
                                  WIND_TEST_CASES]
  --retry TEXT                    Retry failed tests using generated xml file.
                                  [env var: WIND_RETRY]
  --version                       Show the version and exit.
  -h, --help                      Show this message and exit.
```

You can learn more about how to use `WIND` tool and refer associated use-cases [Here](./use-cases/README.md).

## Help

`WIND` tool is meant to be community supported. Feedback is welcome to this repo, please open a PR/Issues if you have any.

## Contributing

This project welcomes contributions from the community. Before submitting a pull
request, please [review our contribution guide](./CONTRIBUTING.md).

## Security

Please consult the [security guide](.github/SECURITY.md) for our responsible security
vulnerability disclosure process.

## License

Copyright (c) 2021 Oracle and/or its affiliates.
Released under the Universal Permissive License v1.0 as shown at
<https://oss.oracle.com/licenses/upl/>.