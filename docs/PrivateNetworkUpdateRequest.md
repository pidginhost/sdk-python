# PrivateNetworkUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway** | **str** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.private_network_update_request import PrivateNetworkUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateNetworkUpdateRequest from a JSON string
private_network_update_request_instance = PrivateNetworkUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PrivateNetworkUpdateRequest.to_json())

# convert the object into a dict
private_network_update_request_dict = private_network_update_request_instance.to_dict()
# create an instance of PrivateNetworkUpdateRequest from a dict
private_network_update_request_from_dict = PrivateNetworkUpdateRequest.from_dict(private_network_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


