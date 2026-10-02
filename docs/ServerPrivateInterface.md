# ServerPrivateInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **str** |  | 
**address** | **str** |  | 
**network** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.server_private_interface import ServerPrivateInterface

# TODO update the JSON string below
json = "{}"
# create an instance of ServerPrivateInterface from a JSON string
server_private_interface_instance = ServerPrivateInterface.from_json(json)
# print the JSON string representation of the object
print(ServerPrivateInterface.to_json())

# convert the object into a dict
server_private_interface_dict = server_private_interface_instance.to_dict()
# create an instance of ServerPrivateInterface from a dict
server_private_interface_from_dict = ServerPrivateInterface.from_dict(server_private_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


