# ResourcePoolAdd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_pool_package** | **str** | ID or slug | 
**resource_pool_size** | **int** |  | 

## Example

```python
from pidginhost_sdk.models.resource_pool_add import ResourcePoolAdd

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcePoolAdd from a JSON string
resource_pool_add_instance = ResourcePoolAdd.from_json(json)
# print the JSON string representation of the object
print(ResourcePoolAdd.to_json())

# convert the object into a dict
resource_pool_add_dict = resource_pool_add_instance.to_dict()
# create an instance of ResourcePoolAdd from a dict
resource_pool_add_from_dict = ResourcePoolAdd.from_dict(resource_pool_add_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


