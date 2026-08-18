# DomainRegistrant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**company** | **str** |  | [optional] 
**address** | **str** |  | 
**city** | **str** |  | 
**region** | **str** |  | 
**postal_code** | **str** |  | 
**country** | [**CountryEnum**](CountryEnum.md) |  | 
**email** | **str** |  | 
**phone** | **str** |  | 
**cif_cnp** | **str** |  | [optional] 
**reg_com** | **str** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.domain_registrant import DomainRegistrant

# TODO update the JSON string below
json = "{}"
# create an instance of DomainRegistrant from a JSON string
domain_registrant_instance = DomainRegistrant.from_json(json)
# print the JSON string representation of the object
print(DomainRegistrant.to_json())

# convert the object into a dict
domain_registrant_dict = domain_registrant_instance.to_dict()
# create an instance of DomainRegistrant from a dict
domain_registrant_from_dict = DomainRegistrant.from_dict(domain_registrant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


