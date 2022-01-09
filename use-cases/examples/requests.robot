*** Settings ***
Resource        ./variables.robot

*** Test Cases ***
Login to OCI Marketplace
    OCI.Generate Auth Token
    ...    base_api_url=${api_url}
    ...    client_id=${client_id} 
    ...    secret_key=${secret_key}
    ...    username=${username}

Get Install Requests
    ${listing_install_requests} =    OCI.Get Application Install Requests
                                     ...    install_status=INSTALLED
                                     ...    listing_id=109XXXX
    Log To Console    ${listing_install_requests}
