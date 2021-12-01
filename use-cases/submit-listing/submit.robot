*** Settings ***
Resource        ../variables.robot

*** Test Cases ***
Login to OCI Marketplace
    OCI.Generate Auth Token
    ...    base_api_url=${api_url}
    ...    client_id=${client_id} 
    ...    secret_key=${secret_key}
    ...    username=${username}

Submit Application
    ${application_submit} =    OCI.Submit Application
    ...    application_name=<your_application_name>
    ...    submitting_note=<your_submitting_note>
    Log To Console    ${application_submit}