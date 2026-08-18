# DomainAdd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**dns_source** | [**DnsSourceEnum**](DnsSourceEnum.md) |  | 
**managed_domain** | **int** |  | [optional] 
**managed_external_domain** | **int** |  | [optional] 
**use_inbound** | **bool** |  | [optional] [default to False]

## Example

```python
from pidginhost_sdk.models.domain_add import DomainAdd

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAdd from a JSON string
domain_add_instance = DomainAdd.from_json(json)
# print the JSON string representation of the object
print(DomainAdd.to_json())

# convert the object into a dict
domain_add_dict = domain_add_instance.to_dict()
# create an instance of DomainAdd from a dict
domain_add_from_dict = DomainAdd.from_dict(domain_add_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


