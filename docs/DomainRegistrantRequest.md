# DomainRegistrantRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from pidginhost_sdk.models.domain_registrant_request import DomainRegistrantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainRegistrantRequest from a JSON string
domain_registrant_request_instance = DomainRegistrantRequest.from_json(json)
# print the JSON string representation of the object
print(DomainRegistrantRequest.to_json())

# convert the object into a dict
domain_registrant_request_dict = domain_registrant_request_instance.to_dict()
# create an instance of DomainRegistrantRequest from a dict
domain_registrant_request_from_dict = DomainRegistrantRequest.from_dict(domain_registrant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


