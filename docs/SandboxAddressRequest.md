# SandboxAddressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.sandbox_address_request import SandboxAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SandboxAddressRequest from a JSON string
sandbox_address_request_instance = SandboxAddressRequest.from_json(json)
# print the JSON string representation of the object
print(SandboxAddressRequest.to_json())

# convert the object into a dict
sandbox_address_request_dict = sandbox_address_request_instance.to_dict()
# create an instance of SandboxAddressRequest from a dict
sandbox_address_request_from_dict = SandboxAddressRequest.from_dict(sandbox_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


