
# Marketplace Auth APIs Keywords

* **Defined in:** [wind_marketplace_library][wind_marketplace_library_link]
* **API Reference**: [Rest API](https://docs.oracle.com/en/cloud/marketplace/partner-portal/rest-api-publisher/QuickStart.html)

### Description
The following keywords are available for operations against **Marketplace** API:

* Generate Auth Token

### Examples

``` 
    Marketplace.Generate Auth Token
    ...    base_api_url=<marketplace_api_url>
    ...    client_id=test
    ...    secret_key=test123
    ...    username=test1234

```

### Parameters

Below tables represents each keyword, associated parameters and their return value: 

- **Generate Auth Token**: 

| Parameters  | Required | Comment                                                                 |
|-------------|----------|-------------------------------------------------------------------------|
| base_api_url| Yes      | Marketplace API URL                                                     |
| client_id   | Yes      | Client ID Value                                                         |
| secret_key  | Yes      | Secret Key Associated to your Account                                   |
| username    | Yes      | Publisher User Name                                                     |
| max_records | No       | Max Applications Record Count; Default 50, Maximum Value allowed is 100 |

This keyword **Return** value is auth token which you will use in consecutive keywords execution. 

[wind_marketplace_library_link]: https://github.com/oracle/wind/tree/main/wind-oci-marketplace/MarketplaceLibrary

