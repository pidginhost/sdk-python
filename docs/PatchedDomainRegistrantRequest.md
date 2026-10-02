# PatchedDomainRegistrantRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**country** | [**CountryEnum**](CountryEnum.md) |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**cif_cnp** | **str** |  | [optional] 
**reg_com** | **str** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.patched_domain_registrant_request import PatchedDomainRegistrantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedDomainRegistrantRequest from a JSON string
patched_domain_registrant_request_instance = PatchedDomainRegistrantRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedDomainRegistrantRequest.to_json())

# convert the object into a dict
patched_domain_registrant_request_dict = patched_domain_registrant_request_instance.to_dict()
# create an instance of PatchedDomainRegistrantRequest from a dict
patched_domain_registrant_request_from_dict = PatchedDomainRegistrantRequest.from_dict(patched_domain_registrant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


