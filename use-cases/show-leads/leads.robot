*** Settings ***
Resource        ../variables.robot

*** Test Cases ***
Login to OCI Marketplace
    OCI.Generate Auth Token
    ...    base_api_url=${api_url}
    ...    client_id=${client_id} 
    ...    secret_key=${secret_key}
    ...    username=${username}

Show Leads
    ${leads} =    OCI.Get Leads
    Log To Console    ${leads}
