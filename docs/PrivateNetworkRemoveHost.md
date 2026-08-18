# PrivateNetworkRemoveHost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server** | **str** | Server hostname or private IP | 

## Example

```python
from pidginhost_sdk.models.private_network_remove_host import PrivateNetworkRemoveHost

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateNetworkRemoveHost from a JSON string
private_network_remove_host_instance = PrivateNetworkRemoveHost.from_json(json)
# print the JSON string representation of the object
print(PrivateNetworkRemoveHost.to_json())

# convert the object into a dict
private_network_remove_host_dict = private_network_remove_host_instance.to_dict()
# create an instance of PrivateNetworkRemoveHost from a dict
private_network_remove_host_from_dict = PrivateNetworkRemoveHost.from_dict(private_network_remove_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


