# PatchedServerDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**hostname** | **str** |  | [optional] [readonly] 
**project** | **str** |  | [optional] 
**image** | **str** |  | [optional] [readonly] 
**package** | **str** |  | [optional] [readonly] 
**cpus** | **int** |  | [optional] [readonly] 
**memory** | **int** |  | [optional] [readonly] 
**disk_size** | **int** |  | [optional] [readonly] 
**machine** | **Dict[str, object]** |  | [optional] [readonly] 
**volumes** | [**List[Volume]**](Volume.md) |  | [optional] [readonly] 
**networks** | **Dict[str, object]** |  | [optional] [readonly] 
**password** | **str** |  | [optional] 
**status** | [**StatusA57Enum**](StatusA57Enum.md) |  | [optional] [readonly] 
**username** | **str** |  | [optional] [readonly] 
**destroy_protection** | **bool** | Prevents the server from being destroyed until disabled. | [optional] [readonly] 
**ha_enabled** | **bool** | Enables Proxmox HA — automatic restart and migration on node failure. | [optional] [readonly] 

## Example

```python
from pidginhost_sdk.models.patched_server_detail import PatchedServerDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedServerDetail from a JSON string
patched_server_detail_instance = PatchedServerDetail.from_json(json)
# print the JSON string representation of the object
print(PatchedServerDetail.to_json())

# convert the object into a dict
patched_server_detail_dict = patched_server_detail_instance.to_dict()
# create an instance of PatchedServerDetail from a dict
patched_server_detail_from_dict = PatchedServerDetail.from_dict(patched_server_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


