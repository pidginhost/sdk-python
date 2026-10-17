# DomainAvailability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** |  | 
**supported** | **bool** |  | 

## Example

```python
from pidginhost_sdk.models.domain_availability import DomainAvailability

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAvailability from a JSON string
domain_availability_instance = DomainAvailability.from_json(json)
# print the JSON string representation of the object
print(DomainAvailability.to_json())

# convert the object into a dict
domain_availability_dict = domain_availability_instance.to_dict()
# create an instance of DomainAvailability from a dict
domain_availability_from_dict = DomainAvailability.from_dict(domain_availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


