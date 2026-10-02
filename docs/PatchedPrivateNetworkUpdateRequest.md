# PatchedPrivateNetworkUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway** | **str** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.patched_private_network_update_request import PatchedPrivateNetworkUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPrivateNetworkUpdateRequest from a JSON string
patched_private_network_update_request_instance = PatchedPrivateNetworkUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedPrivateNetworkUpdateRequest.to_json())

# convert the object into a dict
patched_private_network_update_request_dict = patched_private_network_update_request_instance.to_dict()
# create an instance of PatchedPrivateNetworkUpdateRequest from a dict
patched_private_network_update_request_from_dict = PatchedPrivateNetworkUpdateRequest.from_dict(patched_private_network_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


