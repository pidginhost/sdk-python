# PrivateNetworkAddHost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server** | **str** | Server hostname | 
**address** | **str** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.private_network_add_host import PrivateNetworkAddHost

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateNetworkAddHost from a JSON string
private_network_add_host_instance = PrivateNetworkAddHost.from_json(json)
# print the JSON string representation of the object
print(PrivateNetworkAddHost.to_json())

# convert the object into a dict
private_network_add_host_dict = private_network_add_host_instance.to_dict()
# create an instance of PrivateNetworkAddHost from a dict
private_network_add_host_from_dict = PrivateNetworkAddHost.from_dict(private_network_add_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


