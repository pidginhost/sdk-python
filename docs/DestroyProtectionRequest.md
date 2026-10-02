# DestroyProtectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destroy_protection** | **bool** |  | 

## Example

```python
from pidginhost_sdk.models.destroy_protection_request import DestroyProtectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DestroyProtectionRequest from a JSON string
destroy_protection_request_instance = DestroyProtectionRequest.from_json(json)
# print the JSON string representation of the object
print(DestroyProtectionRequest.to_json())

# convert the object into a dict
destroy_protection_request_dict = destroy_protection_request_instance.to_dict()
# create an instance of DestroyProtectionRequest from a dict
destroy_protection_request_from_dict = DestroyProtectionRequest.from_dict(destroy_protection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


