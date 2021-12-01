# Marketplace Tenancy APIs Keywords
* **Defined in:** [wind_marketplace_library][wind_marketplace_library_link]
* **API Reference**:
[Rest API](https://docs.oracle.com/en/cloud/marketplace/partner-portal/rest-api-publisher/api-tenancy-resources.html)


### Description
The following keywords are available for operations against **Marketplace** API:

* List OCI Tenancies
* Create OCI Tenancy
* Update OCI Tenancy
* Get Tenancy Details 
* Delete Tenancy
* Get Tenancy Compute Images

### Examples

``` 
    Marketplace.List OCI Tenancies

    Marketplace.Create OCI Tenancy
    ...    tenancy_name=my_tenancy
    ...    tenancy_ocid=ocid1.tenancy.XXXXX
    ...    tenancy_home_region_code=IAD
    ...    compartment_ocid=oci.compartment.XXXX

    Marketplace.Update OCI Tenancy
    ...    tenancy_id=99612551
    ...    tenancy_name=my_tenancy
    ...    tenancy_ocid=ocid1.tenancy.XXXXX
    ...    tenancy_home_region_code=IAD
    ...    compartment_ocid=oci.compartment.XXXX

    Marketplace.Get Tenancy Details
    ...    tenancy_id=99612551

    Marketplace.Delete Tenancy
    ...    tenancy_id=99612551

    Marketplace.Get Tenancy Compute Images
    ...    tenancy_id=99612551

```

### Parameters

Below tables represents each keyword, associated parameters and their return value: 

- **List OCI Tenancies**: 

| Parameters | Required | Comment   |
|------------|----------|-----------|
| N/A        | N/A      | N/A       |

This keyword **Return** value is list of OCI tenancies added to your account.

- **Create OCI Tenancy**: 

| Parameters               | Required | Comment                                                            |
|--------------------------|----------|--------------------------------------------------------------------|
| tenancy_name             | Yes      | Friendly Tenancy Name for Marketplace Listing OCI Account          |
| tenancy_ocid             | Yes      | Tenancy OCID wher you have your custom image for listing           |
| tenancy_home_region_code | Yes      | Region where you have your custom image for listing; Example: IAD  |
| compartment_ocid         | Yes      | Compartment OCID where you will have your custom Image for listing |

This keyword **Return** value is a **JSON** tenancy details which you just added to your account.

- **Update OCI Tenancy**: 

| Parameters               | Required | Comment                                                            |
|--------------------------|----------|--------------------------------------------------------------------|
| tenancy_id               | Yes      | Tenancy ID associated with your marketplace publisher account      |
| tenancy_name             | Yes      | Friendly Tenancy Name for Marketplace Listing OCI Account          |
| tenancy_ocid             | Yes      | Tenancy OCID wher you have your custom image for listing           |
| tenancy_home_region_code | Yes      | Region where you have your custom image for listing                |
| compartment_ocid         | Yes      | Compartment OCID where you will have your custom Image for listing |

This keyword **Return** value is a **JSON** message which indicates details successfully updated.

- **Get Tenancy Details**: 

| Parameters | Required | Comment                                                       |
|------------|----------|---------------------------------------------------------------|
| tenancy_id | Yes      | Tenancy ID associated with your marketplace publisher account |

This keyword **Return** value is a **JSON** tenancy details which you just added to your account.

- **Delete Tenancy**: 

| Parameters | Required | Comment                                                       |
|------------|----------|---------------------------------------------------------------|
| tenancy_id | Yes      | Tenancy ID associated with your marketplace publisher account |

This keyword **Return** value is a **JSON** message that your tenancy has deleted.

- **Get Tenancy Compute Images**: 

| Parameters | Required | Comment                                                       |
|------------|----------|---------------------------------------------------------------|
| tenancy_id | Yes      | Tenancy ID associated with your marketplace publisher account |

This keyword **Return** value of compute images list available in your tenancy.


[wind_marketplace_library_link]: https://github.com/oracle/wind/tree/main/wind-oci-marketplace/MarketplaceLibrary