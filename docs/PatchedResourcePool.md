# PatchedResourcePool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**package** | **str** |  | [optional] [readonly] 
**size** | **str** |  | [optional] [readonly] 
**nodes** | [**List[ResourcePoolNode]**](ResourcePoolNode.md) |  | [optional] [readonly] 
**new_size** | **int** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.patched_resource_pool import PatchedResourcePool

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedResourcePool from a JSON string
patched_resource_pool_instance = PatchedResourcePool.from_json(json)
# print the JSON string representation of the object
print(PatchedResourcePool.to_json())

# convert the object into a dict
patched_resource_pool_dict = patched_resource_pool_instance.to_dict()
# create an instance of PatchedResourcePool from a dict
patched_resource_pool_from_dict = PatchedResourcePool.from_dict(patched_resource_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


