*** Settings ***
Resource        ./variables.robot

*** Test Cases ***
Login to OCI Marketplace
    OCI.Generate Auth Token
    ...    base_api_url=${api_url}
    ...    client_id="<your_client_id>"
    ...    secret_key="<your_secret_key>"
    ...    username="<your_username>"