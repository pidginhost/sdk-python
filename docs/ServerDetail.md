# ServerDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**hostname** | **str** |  | [readonly] 
**project** | **str** |  | [optional] 
**image** | **str** |  | [readonly] 
**package** | **str** |  | [readonly] 
**cpus** | **int** |  | [readonly] 
**memory** | **int** |  | [readonly] 
**disk_size** | **int** |  | [readonly] 
**generation** | **str** |  | [readonly] 
**machine** | **Dict[str, object]** |  | [readonly] 
**volumes** | [**List[Volume]**](Volume.md) |  | [readonly] 
**networks** | **Dict[str, object]** |  | [readonly] 
**password** | **str** |  | [optional] 
**status** | [**StatusA57Enum**](StatusA57Enum.md) |  | [readonly] 
**username** | **str** |  | [readonly] 
**destroy_protection** | **bool** | Prevents the server from being destroyed until disabled. | [readonly] 
**ha_enabled** | **bool** | Enables Proxmox HA — automatic restart and migration on node failure. | [readonly] 

## Example

```python
from pidginhost_sdk.models.server_detail import ServerDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ServerDetail from a JSON string
server_detail_instance = ServerDetail.from_json(json)
# print the JSON string representation of the object
print(ServerDetail.to_json())

# convert the object into a dict
server_detail_dict = server_detail_instance.to_dict()
# create an instance of ServerDetail from a dict
server_detail_from_dict = ServerDetail.from_dict(server_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


