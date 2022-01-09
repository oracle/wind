*** Settings ***
Library         MarketplaceLibrary    WITH NAME    OCI

*** Variables ***
##############################
#     LOGIN VARIABLES
##############################

${api_url}                       API_URL
${client_id}                     XXXXXX
${secret_key}                    YYYYYY
${username}                      ZZZZZZ
${tenancy_id}                    654XXXX
${my_tenancy_id}                 111XXXX
${tenancy_name}                  partnere-test
${tenancy_ocid}                  ocid1.tenancy.oc1..XXXXXX
${tenancy_home_region_code}      IAD
${compartment_ocid}              ocid1.compartment.oc1..XXXX