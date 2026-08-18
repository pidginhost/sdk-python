# PatchedDomain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**domain** | **str** |  | [optional] [readonly] 
**tld** | [**TLD**](TLD.md) |  | [optional] [readonly] 
**idna** | **bool** | Domain name is encoded with IDN | [optional] [readonly] 
**nameservers** | **str** | List of 2-5 name-servers separated by comma. | [optional] 
**expiration_date** | **date** |  | [optional] [readonly] 
**registration_date** | **date** |  | [optional] [readonly] 
**service** | [**Service**](Service.md) |  | [optional] [readonly] 
**idna_name** | **str** |  | [optional] [readonly] 
**max_renew_years** | **int** |  | [optional] [readonly] 
**service_status** | **str** | Service status | [optional] [readonly] 
**contacts** | **object** |  | [optional] [readonly] 

## Example

```python
from pidginhost_sdk.models.patched_domain import PatchedDomain

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedDomain from a JSON string
patched_domain_instance = PatchedDomain.from_json(json)
# print the JSON string representation of the object
print(PatchedDomain.to_json())

# convert the object into a dict
patched_domain_dict = patched_domain_instance.to_dict()
# create an instance of PatchedDomain from a dict
patched_domain_from_dict = PatchedDomain.from_dict(patched_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


