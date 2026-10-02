# PrivateNetworkRemoveHostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server** | **str** | Server hostname or private IP | 

## Example

```python
from pidginhost_sdk.models.private_network_remove_host_request import PrivateNetworkRemoveHostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateNetworkRemoveHostRequest from a JSON string
private_network_remove_host_request_instance = PrivateNetworkRemoveHostRequest.from_json(json)
# print the JSON string representation of the object
print(PrivateNetworkRemoveHostRequest.to_json())

# convert the object into a dict
private_network_remove_host_request_dict = private_network_remove_host_request_instance.to_dict()
# create an instance of PrivateNetworkRemoveHostRequest from a dict
private_network_remove_host_request_from_dict = PrivateNetworkRemoveHostRequest.from_dict(private_network_remove_host_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


