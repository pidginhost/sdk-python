# Server


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**hostname** | **str** |  | [optional] 
**project** | **str** |  | [optional] 
**image** | **str** |  | [readonly] 
**package** | **str** |  | [readonly] 
**cpus** | **int** |  | [readonly] 
**memory** | **int** |  | [readonly] 
**disk_size** | **int** |  | [readonly] 
**generation** | **str** |  | [readonly] 
**status** | [**StatusA57Enum**](StatusA57Enum.md) |  | [optional] 
**destroy_protection** | **bool** | Prevents the server from being destroyed until disabled. | [readonly] 
**ha_enabled** | **bool** | Enables Proxmox HA — automatic restart and migration on node failure. | [readonly] 
**networks** | **Dict[str, object]** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.server import Server

# TODO update the JSON string below
json = "{}"
# create an instance of Server from a JSON string
server_instance = Server.from_json(json)
# print the JSON string representation of the object
print(Server.to_json())

# convert the object into a dict
server_dict = server_instance.to_dict()
# create an instance of Server from a dict
server_from_dict = Server.from_dict(server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


