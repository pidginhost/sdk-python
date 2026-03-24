# DomainCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain with tld, ex: example.com | 
**nameservers** | **str** | List of 2-5 name-servers separated by comma. | [optional] 
**years** | **int** |  | [optional] [default to 1]

## Example

```python
from pidginhost_sdk.models.domain_create import DomainCreate

# TODO update the JSON string below
json = "{}"
# create an instance of DomainCreate from a JSON string
domain_create_instance = DomainCreate.from_json(json)
# print the JSON string representation of the object
print(DomainCreate.to_json())

# convert the object into a dict
domain_create_dict = domain_create_instance.to_dict()
# create an instance of DomainCreate from a dict
domain_create_from_dict = DomainCreate.from_dict(domain_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


