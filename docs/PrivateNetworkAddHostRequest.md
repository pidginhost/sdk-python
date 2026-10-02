# PrivateNetworkAddHostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server** | **str** | Server hostname | 
**address** | **str** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.private_network_add_host_request import PrivateNetworkAddHostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateNetworkAddHostRequest from a JSON string
private_network_add_host_request_instance = PrivateNetworkAddHostRequest.from_json(json)
# print the JSON string representation of the object
print(PrivateNetworkAddHostRequest.to_json())

# convert the object into a dict
private_network_add_host_request_dict = private_network_add_host_request_instance.to_dict()
# create an instance of PrivateNetworkAddHostRequest from a dict
private_network_add_host_request_from_dict = PrivateNetworkAddHostRequest.from_dict(private_network_add_host_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


