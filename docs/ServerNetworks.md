# ServerNetworks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public** | [**ServerPublicNetwork**](ServerPublicNetwork.md) |  | 
**private** | [**List[ServerPrivateInterface]**](ServerPrivateInterface.md) |  | 

## Example

```python
from pidginhost_sdk.models.server_networks import ServerNetworks

# TODO update the JSON string below
json = "{}"
# create an instance of ServerNetworks from a JSON string
server_networks_instance = ServerNetworks.from_json(json)
# print the JSON string representation of the object
print(ServerNetworks.to_json())

# convert the object into a dict
server_networks_dict = server_networks_instance.to_dict()
# create an instance of ServerNetworks from a dict
server_networks_from_dict = ServerNetworks.from_dict(server_networks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


