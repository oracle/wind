*** Settings ***
Resource        ./variables.robot

*** Test Cases ***
Login to OCI Marketplace
    OCI.Generate Auth Token
    ...    base_api_url=${api_url}
    ...    client_id=${client_id} 
    ...    secret_key=${secret_key}
    ...    username=${username}

Create Stack Artifiact
    ${create_stack_artifiact} =    OCI.Create Stack Artifact
                                   ...    artifact_name=Partner-Test-22
                                   ...    artifact_file_name=9.0.2.1.zip
                                   ...    artifact_file_path=/Users/user/Desktop/9.0.2.1.zip
    Log To Console    ${create_stack_artifiact}


List All Image Artifacts
    ${image_artifacts} =    OCI.List Image Artifacts
                            ...    limit=10
    Log To Console    ${image_artifacts}

List All Stack Artifacts
    ${stack_artifacts} =    OCI.List Stack Artifacts
                            ...    limit=10
    Log To Console    ${stack_artifacts}

List All Artifacts
    ${all_artifacts} =    OCI.List All Artifacts
    Log To Console        ${all_artifacts}

Create Image Artifact
    ${create_image_artifact} =    OCI.Create Image Artifact
                                  ...    artifact_name=Partner-Test-23
                                  ...    artifact_region_code_name=IAD
                                  ...    artifact_image_ocid=ocid1.image.oc1.iad.XXXX
                                  ...    compartment_ocid=ocid1.compartment.oc1..YYYY
                                  ...    tenancy_id=758XXXX
                                  ...    compatible_shapes=VM.Standard2.2,VM.Standard2.4
    Log To Console    ${create_image_artifact}

Get Artifact Details
    ${artifact_details} =    OCI.Get Artifact By ID
                             ...    artifact_id=1110XXX
    Log To Console    ${artifact_details}

Delete Artifact 
    ${delete_artifact} =    OCI.Delete Artifact
                            ...    artifact_id=1110YYYY
    Log To Console    ${delete_artifact}
