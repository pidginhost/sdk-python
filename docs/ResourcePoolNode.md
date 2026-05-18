# ResourcePoolNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**ip** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.resource_pool_node import ResourcePoolNode

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcePoolNode from a JSON string
resource_pool_node_instance = ResourcePoolNode.from_json(json)
# print the JSON string representation of the object
print(ResourcePoolNode.to_json())

# convert the object into a dict
resource_pool_node_dict = resource_pool_node_instance.to_dict()
# create an instance of ResourcePoolNode from a dict
resource_pool_node_from_dict = ResourcePoolNode.from_dict(resource_pool_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


