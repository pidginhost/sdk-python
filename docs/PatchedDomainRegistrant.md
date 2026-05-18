# PatchedDomainRegistrant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
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
from pidginhost_sdk.models.patched_domain_registrant import PatchedDomainRegistrant

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedDomainRegistrant from a JSON string
patched_domain_registrant_instance = PatchedDomainRegistrant.from_json(json)
# print the JSON string representation of the object
print(PatchedDomainRegistrant.to_json())

# convert the object into a dict
patched_domain_registrant_dict = patched_domain_registrant_instance.to_dict()
# create an instance of PatchedDomainRegistrant from a dict
patched_domain_registrant_from_dict = PatchedDomainRegistrant.from_dict(patched_domain_registrant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


