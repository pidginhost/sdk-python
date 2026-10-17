# ExpiringDomain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**expiration_date** | **date** |  | 

## Example

```python
from pidginhost_sdk.models.expiring_domain import ExpiringDomain

# TODO update the JSON string below
json = "{}"
# create an instance of ExpiringDomain from a JSON string
expiring_domain_instance = ExpiringDomain.from_json(json)
# print the JSON string representation of the object
print(ExpiringDomain.to_json())

# convert the object into a dict
expiring_domain_dict = expiring_domain_instance.to_dict()
# create an instance of ExpiringDomain from a dict
expiring_domain_from_dict = ExpiringDomain.from_dict(expiring_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


