# ServerPublicNetwork


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **str** |  | [optional] 
**ipv4** | **str** |  | [optional] 
**ipv6** | **str** |  | [optional] 
**interfaces** | [**List[ServerPublicInterface]**](ServerPublicInterface.md) |  | [optional] 

## Example

```python
from pidginhost_sdk.models.server_public_network import ServerPublicNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of ServerPublicNetwork from a JSON string
server_public_network_instance = ServerPublicNetwork.from_json(json)
# print the JSON string representation of the object
print(ServerPublicNetwork.to_json())

# convert the object into a dict
server_public_network_dict = server_public_network_instance.to_dict()
# create an instance of ServerPublicNetwork from a dict
server_public_network_from_dict = ServerPublicNetwork.from_dict(server_public_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


