*** Settings ***
Resource        ./variables.robot

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

Show Lead Notes
    ${lead_notes} =    OCI.List Lead Notes
                       ...    lead_id=7375XXXX
    Log To Console    ${lead_notes}

Create Lead Notes
    ${lead_notes} =    OCI.Create Lead Notes
                       ...    lead_id=7375XXXX
                       ...    message=This is new note.
    Log To Console    ${lead_notes}

Update Lead Status Value
    ${lead_status} =    OCI.Update Lead Status
                        ...    lead_id=7375XXXX
                        ...    status=Contacted
    Log To Console    ${lead_status}

Delete Lead 
    ${delete_lead} =    OCI.Delete Lead
                        ...    lead_id=7375XXXX
    Log To Console    ${delete_lead}
