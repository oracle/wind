# Introduction

Make sure you have installed `WIND` tool local to your environment and while using this tool you can follow below instructions as a reference point:

> Every test case/suite file must include a Settings section with below value in order to import all WIND OCI Marketplace Library keywords.

```
Library         MarketplaceLibrary    WITH NAME    OCI
```

> You can also import OCI Marketplace Library with different name as below:

```
Library         MarketplaceLibrary    WITH NAME    Marketplace
```

This snippet is an example of a WIND test suite and how to use `WIND OCI Marketplace Library`. 

```
*** Settings ***
Library         MarketplaceLibrary    WITH NAME    Marketplace

*** Test Cases ***
Connect to Setup
    Marketplace.Generate Auth Token
    ...    base_api_url=<your_marketplace_api_url>
    ...    client_id=<your_client_id>
    ...    secret_key=<your_client_key>
    ...    username=<your_username>
```

To run a simple test suite named `login.robot`:

```shell
user@machine:~$ wind use-cases/authentication/login.robot --log-level=debug
==============================================================================
Login                                                                         
==============================================================================
Login to OCI Marketplace                                              | PASS |
------------------------------------------------------------------------------
Login                                                                 | PASS |
1 critical test, 1 passed, 0 failed
1 test total, 1 passed, 0 failed
==============================================================================
Output:  test_reports/wind-output-20211017-180632.xml
Log:     test_reports/wind-log-20211017-180632.html
Report:  test_reports/wind-report-20211017-180632.html
```

`WIND` can also be used in other python programs when imported as a library. **`Python 2.x` is not supported**.

```python
from wind.wind import Wind

wind_runner = Wind(
    "test_suites/my_example_test_suite",
    "0.0.1",
    "0.0.1",
)

wind_runner.execute(dry_run=True)
```

## Use-Cases

We have written some use-cases which you can refer to support automation around OCI Marektplace Partner Portal:

- **Authentication** : [marketplace-authentication](./authentication) this allows end user to authenticate.
- **Submit Listing** : [submit-listing](./submit-listing) this allows end user to submit listings.
- **Show Leads** : [show-leads](./show-leads) this allows end user to Show Leads.

You can refer to more **Examples** [Here](./examples/README.md).