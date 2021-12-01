# Marketplace Lead APIs Keywords
* **Defined in:** [wind_marketplace_library][wind_marketplace_library_link]
* **API Reference**:
[Rest API](https://docs.oracle.com/en/cloud/marketplace/partner-portal/rest-api-publisher/api-lead-resources.html)


### Description
The following keywords are available for operations against **Marketplace** API:

* Get Leads Reports
* Get Leads
* Create Lead Notes 
* Update Lead Status
* List Lead Notes
* Delete Lead 

### Examples

``` 
    Marketplace.Get Leads Reports
    ...    group_by=DATE
    ...    time_type=MONTHLY

    Marketplace.Get Leads

    Marketplace.Create Lead Notes
    ...    lead_id=73751XXX
    ...    message=This is new Note.

    Marketplace.Update Lead Status
    ...    lead_id=73751XXX
    ...    status=Contacted

    Marketplace.List Lead Notes
    ...    lead_id=73751XXX

    Marketplace.Delete Lead 
    ...    lead_id=73751XXX

```

### Parameters

Below tables represents each keyword, associated parameters and their return value: 

- **Get Leads Reports**: 

| Parameters           | Required | Comment                                                                                            |
|----------------------|----------|----------------------------------------------------------------------------------------------------|
| createdOnRangeStart  | No       | Start Date; Example: 2016-01-01 i.e. YYYY-MM-DD                                                    |
| createdOnRangeEnd    | No       | End Date; Example: 2016-01-01 i.e. YYYY-MM-DD                                                      |
| group_by             | Yes      | Report group type; DATE, STATUS, LISTING                                                           |
| time_type            | No       | Time type; MONTHLY, WEEKLY, DAILY                                                                  |

This keyword **Return** value is list of lead reports present in your account. 

- **Get Leads**: 

| Parameters           | Required | Comment                                                                                            |
|----------------------|----------|----------------------------------------------------------------------------------------------------|
| createdOnRangeStart  | No       | Start Date; Example: 2016-01-01 i.e. YYYY-MM-DD                                                    |
| createdOnRangeEnd    | No       | End Date; Example: 2016-01-01 i.e. YYYY-MM-DD                                                      |
| orderby              | No       | Show Leads in Order; NAME, COMPANY, LAST_NAME, FIRST_NAME, CREATION_DATE,LASTMODIFIED_DATE         |
| sortorder            | No       | Short Leads in Order: ASC, DSC                                                                     |
| keywordValue         | No       | Any Valid String                                                                                   |
| listingtype          | No       | Listing Type; APPLICATION, SERVICE                                                                 |
| status               | No       | Status of Lead: NEW, CONTACTED, PURCHASED, DELIVERED                                               |

This keyword **Return** value is list leads present in your account. 

- **Create Lead Notes**: 

| Parameters     | Required | Comment                    |
|----------------|----------|----------------------------|
| lead_id        | Yes      | Lead ID                    |
| message        | Yes      | Note message.              | 

This keyword **Return** value is a successful message and lead ID.

- **Update Lead Status**: 

| Parameters     | Required | Comment                                       |
|----------------|----------|-----------------------------------------------|
| lead_id        | Yes      | Lead ID                                       |
| status         | Yes      | Lead Status; Contacted, Purchased, Delivered. | 

This keyword **Return** value is a successful message and lead ID.

- **List Lead Notes**: 

| Parameters     | Required | Comment                    |
|----------------|----------|----------------------------|
| lead_id        | Yes      | Lead ID                    |

This keyword **Return** value is a list of Lead Notes. 

- **Delete Lead**: 

| Parameters     | Required | Comment                    |
|----------------|----------|----------------------------|
| lead_id        | Yes      | Lead ID                    |

This keyword **Return** value is a successful message and lead ID.


[wind_marketplace_library_link]: https://github.com/oracle-quickstart/oci-marketplace-wind