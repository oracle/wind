# Marketplace Terms APIs Keywords
* **Defined in:** [wind_marketplace_library][wind_marketplace_library_link]
* **API Reference**:
[Rest API](https://docs.oracle.com/en/cloud/marketplace/partner-portal/rest-api-publisher/api-terms-resources.html)


### Description
The following keywords are available for operations against **Marketplace** API:

* Create Terms of Use
* Create New Version of Terms of Use
* Update Version of Terms of Use
* Get All Terms of Use
* Get Terms Version
* Activate Terms of Use
* Deactivate Terms of Use
* Delete Version of Terms of Use

### Examples

``` 
    Marketplace.Create Terms of Use
    ...    version_value=version1
    ...    term_file_path=${CURDIR}/files/term.txt

    Marketplace.Create New Version of Terms of Use
    ...    terms_id=99615508
    ...    version_value=version1.1
    ...    term_file_path=${CURDIR}/files/term.txt

    Marketplace.Update Version of Terms of Use
    ...    terms_id=99615508
    ...    version_value=version1.1
    ...    term_file_path=${CURDIR}/files/term.txt

    Marketplace.Get All Terms of Use

    Marketplace.Get Terms Version
    ...    terms_id=99615599
    ...    terms_version_id=99615599

    Marketplace.Activate Terms of Use
    ...    terms_id=99615599

    Marketplace.Deactivate Terms of Use
    ...    terms_id=99615599

    Marketplace.Delete Version of Terms of Use
    ...    terms_id=99615599
    ...    terms_version_id=99615599

```

### Parameters
Below tables represents each keyword, associated parameters and their return value: 

- **Create Terms of Use**: 

| Parameters     | Required | Comment                                |
|----------------|----------|----------------------------------------|
| version_value  | Yes      | Terms of Use Version Value             |
| term_file_path | Yes      | Terms of Use present in .txt file path |

This keyword **Return** value is a successful message with term ID and name of term. 

- **Create New Version of Terms of Use**: 

| Parameters     | Required | Comment                                |
|----------------|----------|----------------------------------------|
| terms_id       | Yes      | Terms ID                               |
| version_value  | Yes      | Terms of Use Version Value             |
| term_file_path | Yes      | Terms of Use present in .txt file path |

This keyword **Return** value is a successful message with term ID and name of term. 

- **Update Version of Terms of Use**: 

| Parameters     | Required | Comment                     |
|----------------|----------|-----------------------------|
| terms_id       | Yes      | Terms ID                    |
| version_value  | Yes      | Terms of Use Version Value  |
| term_file_path | Yes      | Terms of Use .txt file path |

This keyword **Return** value is a successful message with term ID and name of term. 

- **Get All Terms of Use**: 

| Parameters | Required | Comment   |
|------------|----------|-----------|
| N/A        | N/A      | N/A       |

This keyword **Return** value is list of terms of use available in your account. 

- **Get Terms Version**: 

| Parameters        | Required | Comment                     |
|-------------------|----------|-----------------------------|
| terms_id          | Yes      | Terms ID                    |
| terms_version_id  | Yes      | Terms of Use Version Value  |

This keyword **Return** value is details of particular terms and associated version. 

- **Activate Terms of Use**: 

| Parameters        | Required | Comment                     |
|-------------------|----------|-----------------------------|
| terms_id          | Yes      | Terms ID                    |

This keyword **Return** value is a successfull message and terms details. 

- **Deactivate Terms of Use**: 

| Parameters        | Required | Comment                     |
|-------------------|----------|-----------------------------|
| terms_id          | Yes      | Terms ID                    |

This keyword **Return** value is a successfull message and terms details. 

- **Delete Version of Terms of Use**: 

| Parameters        | Required | Comment                     |
|-------------------|----------|-----------------------------|
| terms_id          | Yes      | Terms ID                    |
| terms_version_id  | Yes      | Terms of Use Version Value  |


[wind_marketplace_library_link]: https://github.com/oracle/wind/tree/main/wind-oci-marketplace/MarketplaceLibrary