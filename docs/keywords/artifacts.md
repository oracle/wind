# Marketplace Artifact APIs Keywords
* **Defined in:** [wind_marketplace_library][wind_marketplace_library_link]
* **API Reference**:
[Rest API](https://docs.oracle.com/en/cloud/marketplace/partner-portal/rest-api-publisher/api-artifact-resources.html)


### Description
The following keywords are available for operations against **Marketplace** API:

* List All Artifacts
* List Image Artifacts
* List Stack Artifacts
* Create Image Artifact
* Create Stack Artifact
* Get Artifact Details
* Delete Artifact

### Examples

``` 
    Marketplace.List All Artifacts
    ...    limit=5

    Marketplace.List Image Artifacts
    ...    limit=5

    Marketplace.List Stack Artifacts
    ...    limit=5

    Marketplace.Create Image Artifact
    ...    artifact_name=test-code
    ...    artifact_region_code_name=IAD
    ...    artifact_image_ocid=ocid1.image.oc1.XXX
    ...    compartment_ocid=ocid1.compartment.oc1.XXXX
    ...    tenancy_id=454545
    ...    compatible_shapes=VM.Standard2.2,VM.Standard2.4

    Marketplace.Create Stack Artifact
    ...    artifact_name=artifact-name
    ...    artifact_file_name=zip_file_name
    ...    artifact_file_path=<zip_file_path>

    Marketplace.Get Artifact Details
    ...    artifact_id=99989689

    Marketplace.Delete Artifact
    ...    artifact_id=99989689

```

### Parameters
Below tables represents each keyword, associated parameters and their return value: 

- **List All Artifacts**: 

| Parameters     | Required | Comment                                      |
|----------------|----------|----------------------------------------------|
| Limit          | No       | Listings Number You want to see. Range 1-100 |

This keyword **Return** value is list of artificats available in your account. 

- **List Image Artifacts**: 

| Parameters     | Required | Comment                                       |
|----------------|----------|-----------------------------------------------|
| Limit          | No       | Listings Number You want to see.  Range 1-100 |

This keyword **Return** value is a successful list of OCI compute image artifacts. 

- **List Stack Artifacts**: 

| Parameters     | Required | Comment                                       |
|----------------|----------|-----------------------------------------------|
| Limit          | No       | Listings Number You want to see.  Range 1-100 |

This keyword **Return** value is a successful list of Terraform Templates artifacts. 

- **Create Image Artifact**: 

| Parameters                   | Required | Comment                                            |
|------------------------------|----------|----------------------------------------------------|
| artifact_name                | Yes      | Artifact Name                                      |
| artifact_region_code_name    | Yes      | Artifact Region Code Name: IAD for Example         |
| artifact_image_ocid          | Yes      | Artifact Image OCID                                |
| compartment_ocid             | Yes      | Artifact Compartment OCID                          |
| tenancy_id                   | Yes      | Artifact Tenancy ID where Custom Image is Present  |
| compatible_shapes            | Yes      | Artifact Comptaible Shapes Seperated by Commas; Example: VM.Standard2.2,VM.Standard2.4   |

This keyword **Return** value is a details of a created image artifact. 

- **Create Stack Artifact**: 

| Parameters                   | Required | Comment                         |
|------------------------------|----------|---------------------------------| 
| artifact_name                | Yes      | Artifact Name                   |
| artifact_file_name           | Yes      | Artifact File Name              |
| artifact_file_path           | Yes      | Artifact File Path              |

This keyword **Return** value is a details of a created stack artifact. 

- **Get Artifacts Details**: 

| Parameters     | Required | Comment       |
|----------------|----------|---------------|
| artifact_id    | Yes      | Artifact ID   |

This keyword **Return** value is a details of a particular artifact using ID.

- **Delete Artifact**: 

| Parameters     | Required | Comment       |
|----------------|----------|---------------|
| artifact_id    | Yes      | Artifact ID   |

This keyword **Return** value is a successful message that particular artifact got deleted. 


[wind_marketplace_library_link]: https://github.com/oracle/wind/tree/main/wind-oci-marketplace/MarketplaceLibrary