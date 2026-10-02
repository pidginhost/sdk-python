# ServerPublicInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **str** |  | 
**ipv4** | **str** |  | 
**ipv6** | **str** |  | 
**primary** | **bool** |  | 

## Example

```python
from pidginhost_sdk.models.server_public_interface import ServerPublicInterface

# TODO update the JSON string below
json = "{}"
# create an instance of ServerPublicInterface from a JSON string
server_public_interface_instance = ServerPublicInterface.from_json(json)
# print the JSON string representation of the object
print(ServerPublicInterface.to_json())

# convert the object into a dict
server_public_interface_dict = server_public_interface_instance.to_dict()
# create an instance of ServerPublicInterface from a dict
server_public_interface_from_dict = ServerPublicInterface.from_dict(server_public_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


