*** Settings ***
Resource        ./variables.robot

*** Test Cases ***
Login to OCI Marketplace
    OCI.Generate Auth Token
    ...    base_api_url=${api_url}
    ...    client_id=${client_id} 
    ...    secret_key=${secret_key}
    ...    username=${username}

List All Tenancies
    ${tenancies} =    OCI.List OCI Tenancies
    Log To Console    ${tenancies}

Add OCI Tenancy
    ${add_tenancy} =    OCI.Create OCI Tenancy
                        ...    tenancy_name=${tenancy_name} 
                        ...    tenancy_ocid=${tenancy_ocid} 
                        ...    tenancy_home_region_code=${tenancy_home_region_code}
                        ...    compartment_ocid=${compartment_ocid} 
    Log To Console    ${add_tenancy}

Update OCI Tenancy
    ${update_tenancy} =      OCI.Update OCI Tenancy
                             ...    tenancy_id=1110XXXX
                             ...    tenancy_name=partner-test
                             ...    tenancy_ocid=${tenancy_ocid} 
                             ...    tenancy_home_region_code=${tenancy_home_region_code}
                             ...    compartment_ocid=${compartment_ocid} 
    Log To Console    ${update_tenancy}

Get Tenancy Details
    ${get_tenancy_details} =      OCI.Get Tenancy Details
                                  ...    tenancy_id=${my_tenancy_id}
    Log To Console    ${get_tenancy_details}

Get Tenancy Compute Images
    ${get_tenancy_custom_images} =      OCI.Get Tenancy Compute Images
                                        ...    tenancy_id=${my_tenancy_id}
                                        ...    tenancy_home_region_code=${tenancy_home_region_code}
                                        ...    compartment_ocid=${compartment_ocid} 
    Log To Console    ${get_tenancy_custom_images}

Delete Tenancy
    ${delete_tenancy} =      OCI.Delete Tenancy
                             ...    tenancy_id=${my_tenancy_id}
    Log To Console    ${delete_tenancy}