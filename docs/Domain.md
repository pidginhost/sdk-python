# Domain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**domain** | **str** |  | [readonly] 
**tld** | [**TLD**](TLD.md) |  | [readonly] 
**idna** | **bool** | Domain name is encoded with IDN | [readonly] 
**nameservers** | **str** | List of 2-5 name-servers separated by comma. | [optional] 
**expiration_date** | **date** |  | [readonly] 
**registration_date** | **date** |  | [readonly] 
**service** | [**Service**](Service.md) |  | [readonly] 
**idna_name** | **str** |  | [readonly] 
**max_renew_years** | **int** |  | [readonly] 
**service_status** | **str** | Service status | [readonly] 
**contacts** | **object** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.domain import Domain

# TODO update the JSON string below
json = "{}"
# create an instance of Domain from a JSON string
domain_instance = Domain.from_json(json)
# print the JSON string representation of the object
print(Domain.to_json())

# convert the object into a dict
domain_dict = domain_instance.to_dict()
# create an instance of Domain from a dict
domain_from_dict = Domain.from_dict(domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


