*** Settings ***
Resource        ./variables.robot

*** Test Cases ***
Login to OCI Marketplace
    OCI.Generate Auth Token
    ...    base_api_url=${api_url}
    ...    client_id=${client_id} 
    ...    secret_key=${secret_key}
    ...    username=${username}

Create Term of Use
    ${terms} =    OCI.Create Terms of Use
                      ...    version_value=Version1
                      ...    term_file_path=${CURDIR}/files/term1.txt
    Log To Console    ${terms}

Activate Particular Terms of Use
    ${activate_terms} =    OCI.Activate Terms of Use
                           ...    terms_id=<termsId>
    Log To Console    ${activate_terms}

Get All Terms of Use
    ${get_terms} =    OCI.Get All Terms of Use
    Log To Console    ${get_terms}

Get Particular Terms of Use
    ${get_term_version} =    OCI.Get Terms Version
                             ...    terms_id=<termsId>
                             ...    terms_version_id=<termsVersionId>
    Log To Console    ${get_term_version}

Create a Version of Existing Term
    ${create_term_version} =    OCI.Create New Version of Terms of Use
                                ...    terms_id=<termsId>
                                ...    version_value=Version2
                                ...    term_file_path=${CURDIR}/files/term1.txt
    Log To Console    ${create_term_version}

Deactivate Particular Terms of Use
    ${deactivate_term} =    OCI.Deactivate Terms of Use
                            ...    terms_id=<termsId>
    Log To Console    ${deactivate_term}

Delete Particular Terms of Use and Version
    ${delete_particular_term_version} =    OCI.Delete Version of Terms of Use
                                           ...    terms_id=<termsId>
                                           ...    terms_version_id=<termsVersionId>
    Log To Console    ${delete_particular_term_version}