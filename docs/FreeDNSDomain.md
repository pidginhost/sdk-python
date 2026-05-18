# FreeDNSDomain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | [readonly] 
**active** | **bool** |  | [readonly] [default to True]
**source** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.free_dns_domain import FreeDNSDomain

# TODO update the JSON string below
json = "{}"
# create an instance of FreeDNSDomain from a JSON string
free_dns_domain_instance = FreeDNSDomain.from_json(json)
# print the JSON string representation of the object
print(FreeDNSDomain.to_json())

# convert the object into a dict
free_dns_domain_dict = free_dns_domain_instance.to_dict()
# create an instance of FreeDNSDomain from a dict
free_dns_domain_from_dict = FreeDNSDomain.from_dict(free_dns_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


