# Marketplace Application APIs Keywords
* **Defined in:** [wind_marketplace_library][wind_marketplace_library_link]
* **API Reference**:
[Rest API](https://docs.oracle.com/en/cloud/marketplace/partner-portal/rest-api-publisher/api-application-resources.html)


### Description

The following keywords are available for operations against **Marketplace** API:

* List Applications 
* Create Application
* Add Application Icon
* Add Application Banner
* Create Application Version
* Get Application Status
* Get Application Details
* Submit Application
* Publish Application
* Withdraw Application
* Delete Application
* Get Application Packages
* Create Application Package
* Add Image Artifact to Application Package
* Add Stack Artifact to Application Package
* Delete Application Package

### Examples

``` 
    Marketplace.List Applications

    Marketplace.Create Application
    ...    name=application_name
    ...    short_description=This is short description. 
    ...    long_description=This is long description.
    ...    usage_information=This is usage instructions.
    ...    tags=Tag1
    ...    pricing_type=PAYGO
    ...    cataegory_name=SECURITY
    ...    tag_line=Security Software | Sales Enablement

    Marketplace.Add Application Icon
    ...    application_name=application_name
    ...    icon_path=file_path
    ...    icon_file_name=file_name

    Marketplace.Add Application Banner
    ...    application_name=application_name
    ...    banner_name=banner_name
    ...    icon_path=file_path
    ...    icon_file_name=file_name

    Marketplace.Create Application Version
    ...    application_id=application_id

    Marketplace.Get Application Status
    ...    application_name=application_name

    Marketplace.Get Application Details
    ...    application_name=application_name

    Marketplace.Submit Application
    ...    application_name=application_name
    ...    submitting_note=Submitting the Appllication

    Marketplace.Publish Application
    ...    application_id=application_id_value

    Marketplace.Withdraw Application
    ...    application_id=application_id_value

    Marketplace.Delete Application
    ...    application_name=application_name

    Marketplace.Create Application Package
    ...    application_name=application_name
    ...    description=This is New Package.
    ...    version=V1.4
    ...    package_type=OCIOrchestration
    ...    terms_id=76209529
    ...    is_security_fix=YES

```

### Parameters

Below tables represents each keyword, associated parameters and their return value: 

- **List Application**: 

| Parameters     | Required | Comment                                              |
|----------------|----------|------------------------------------------------------|
| Status         | No      | Application Status: NEW,PUBLISHED,UNPUBLISHED         |

This keyword **Return** value is list of applications and you can filter them based on application status.

- **Create Application**: 

| Parameters        | Required | Comment                                                                |
|-------------------|----------|------------------------------------------------------------------------|
| name              | Yes      | Application Name                                                       |
| short_description | Yes      | Application Short Description                                          |
| long_description  | Yes      | Application Long Description                                           |
| usage_information | Yes      | Application Usage Information                                          |
| tags              | Yes      | Application Tags: Example: Security                                    |
| tag_line          | Yes      | Application Tag Line: Example: Security                                |
| cataegory_name    | Yes      | Application Category name in Captial Letter: Example: SECURITY         |

> **Note**: Currently **OCI** and associated categories are supported. 

This keyword **Return** value reflects application created successfully.

- **Add Application Icon**: 

| Parameters      | Required  | Comment                                         |
|-----------------|-----------|-------------------------------------------------|
| application_name| Yes       | Application Name where you want to add Banner   |
| icon_path       | Yes       | Banner icon path; Size                                 |
| icon_file_name  | Yes       | Banner Icon File Name                           |

This keyword **Return** value is a successful message of uploading application icon. 

> **Note**: Upload icon as per allowed size on Partner Portal. Check official docs to know more about it.

- **Add Application Banner**: 

| Parameters      | Required  | Comment                                         |
|-----------------|-----------|-------------------------------------------------|
| application_name| Yes       | Application Name where you want to add Banner   |
| banner_name     | Yes       | Application Banner Name                         |
| icon_path       | Yes       | Banner icon path; Size                          |
| icon_file_name  | Yes       | Banner Icon File Name                           |

This keyword **Return** value is a successful message of uploading application banner. 

> **Note**: Upload Banner as per allowed size on Partner Portal. Check official docs to know more about it.

- **Create Application Version**: 

| Parameters      | Required  | Comment                                                  |
|-----------------|-----------|----------------------------------------------------------|
| application_id  | Yes       | Application ID where you want create another version     |

This keyword **Return** value is a successful message of creating another version of existing application.

- **Get Application Status**: 

| Parameters      | Required  | Comment                                                  |
|-----------------|-----------|----------------------------------------------------------|
| application_name| Yes       | Application Name                                         |

This keyword **Return** prints application status. 

- **Get Application Details**: 

| Parameters      | Required  | Comment                                                  |
|-----------------|-----------|----------------------------------------------------------|
| application_name| Yes       | Application Name                                         |

This keyword **Return** prints application details. 

- **Submit Application**: 

| Parameters      | Required  | Comment                                                  |
|-----------------|-----------|----------------------------------------------------------|
| application_name| Yes       | Application Name                                         |
| submitting_note | Yes       | Submitting Note of your Application                      |

This keyword **Return** shows a successful message of application submission. 

- **Publish Application**: 

| Parameters      | Required  | Comment                                                  |
|-----------------|-----------|----------------------------------------------------------|
| application_id  | Yes       | Application ID                                           |

This keyword **Return** shows a successful message of application publication. 

- **Withdraw Application**: 

| Parameters      | Required  | Comment                                                  |
|-----------------|-----------|----------------------------------------------------------|
| application_id  | Yes       | Application ID                                           |

This keyword **Return** prints application details. 

- **Delete Application**: 

| Parameters      | Required  | Comment                                                  |
|-----------------|-----------|----------------------------------------------------------|
| application_name| Yes       | Application Name                                         |

This keyword **Return** displays successful application deletion. 

- **Create Application Package**: 

| Parameters        | Required | Comment                                                                |
|-------------------|----------|------------------------------------------------------------------------|
| application_name  | Yes      | Application Name                                                       |
| description       | Yes      | Package Description                                                    |
| version           | Yes      | Package Version                                                        |
| package_type      | Yes      | Package Type; Terraform listing: OCIOrchestration, Image Listing: OCI  |
| terms_id          | Yes      | Application Tags: Example: Security                                    |
| is_security_fix   | No       | Default Value: False. Allowed Value: YES                               |

This keyword **Return** value reflects successful message of package being part of listing.

### Update Docs for Below Keywords
* Add Image Artifact to Application Package
* Add Stack Artifact to Application Package
* Delete Application Package

[wind_marketplace_library_link]: https://github.com/oracle/wind/tree/main/wind-oci-marketplace/MarketplaceLibrary