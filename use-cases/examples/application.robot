*** Settings ***
Resource        ./variables.robot

*** Test Cases ***
Login to OCI Marketplace
    OCI.Generate Auth Token
    ...    base_api_url=${api_url}
    ...    client_id=${client_id} 
    ...    secret_key=${secret_key}
    ...    username=${username}
    ...    max_records=100

Create Listing For Partner
    ${create_listing} =    OCI.Create Application
                           ...    name=Partner-Test-21
                           ...    short_description=Partner Details2
                           ...    long_description=Partner Details3
                           ...    usage_information=Partner Details4
                           ...    tags=Partner Details5
                           ...    pricing_type=PAYGO
                           ...    cataegory_name=SECURITY
                           ...    tag_line=Security Software | Sales Enablement
    Log To Console    ${create_listing}

Create Package For Partner Listing
    ${create_listing_package} =    OCI.Create Application Package
                                   ...    application_name=Partner-Test-22
                                   ...    description=Test
                                   ...    version=V1.4
                                   ...    package_type=OCIOrchestration
                                   ...    terms_id=7620XXX
                                   #...    is_security_fix=YES
    Log To Console    ${create_listing_package}

Get Partner Listing Packages Details
    ${get_application} =    OCI.Get Application Packages
                            ...    application_name=Partner-Test-21
    Log To Console    ${get_application}

Add Image Artifact to Partner Listing Package
    ${add_image_artifact} =    OCI.Add Image Artifact to Application Package
                               ...    application_name=Partner-Test-21
                               ...    package_id=11196XXX
                               ...    image_artifact_name=OracleLinux8
                               ...    image_artifact_id=1117XXX
    Log To Console    ${add_image_artifact}

Add Stack Artifact to Partner Listing Package
    ${add_stack_artifact} =    OCI.Add Stack Artifact to Application Package
                               ...    application_name=Partner-Test-21
                               ...    package_id=11196XXXX
                               ...    stack_artifact_name=Partner-Stack-22
                               ...    stack_artifact_id=1117XXX
    Log To Console    ${add_stack_artifact}

Delete Partner Listing Package 
    ${delete_listing_package} =    OCI.Delete Application Package
                                   ...    application_name=Partner-Stack-21
                                   ...    package_id=11196XXX
    Log To Console    ${delete_listing_package}

Get Partner Listing Status
    ${get_listing_status} =    OCI.Get Application Status
                               ...    application_name=Palo-Alto-Test
    Log To Console    ${get_listing_status}

List Partner All Listings
    ${applications} =    OCI.List Applications
                         #...    status=UNPUBLISHED
                         #...    limit=100
    Log To Console    ${applications}

Get Partner Listings Details
    ${get_listing_details} =    OCI.Get Application Details
                                ...    application_name=Partner-Test-21
    Log To Console    ${get_listing_details}

## Recommended to use unique task name to avoid duplicate. 
## This is just an Example.
Get Partner Listing Status
    ${get_listing_status} =    OCI.Get Application Status
                               ...    application_name=Partner-Test2
    Log To Console    ${get_listing_status}

Delete Partner Listing
    ${delete_listing} =    OCI.Delete Application
                           ...    application_name=Partner-Test2
    Log To Console    ${delete_listing}

## Your icon must be 130 pixels by 130 pixels, 
## a maximum of 5 MB, and must be a BMP, GIF, JPEG (JPG), or PNG file.

Upload Icon to My Listings
    ${upload_icon_to_listing} =    OCI.Add Application Icon
                                   ...    application_name=Partner-Test-21
                                   ...    icon_path=/Users/user/Desktop/logo.png 
                                   ...    icon_file_name=logo.png
    Log To Console    ${upload_icon_to_listing}

## Your banner must be 1160 pixels (width) by 200 pixels (height), 
## a maximum of 10 MB, and must be a BMP, GIF, JPEG (JPG), or PNG file.

Upload Banner to My Application
    ${upload_banner_to_listing} =    OCI.Add Application Banner
                                     ...    application_name=Partner-Test-21
                                     ...    banner_name=Test This
                                     ...    icon_path=/Users/user/Desktop/banner.png 
                                     ...    icon_file_name=banner.png
    Log To Console    ${upload_banner_to_listing}

Submit My Application
    ${submit_application} =    OCI.Submit Application
                               ...    application_name=Partner-Test-21
                               ...    submitting_note=Submitting the Appllication
    Log To Console    ${submit_application}

Get My Application Status on Submission
    ${get_application_status} =    OCI.Get Application Status
                                   ...    application_name=Partner-Test-21
    Log To Console    ${get_application_status}

Delete My Fortinet Application
    ${delete_application} =    OCI.Delete Application
                               ...    application_name=Partner-Test-211
    Log To Console    ${delete_application}
