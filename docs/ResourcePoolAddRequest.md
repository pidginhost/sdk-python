# ResourcePoolAddRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_pool_package** | **str** | ID or slug | 
**resource_pool_size** | **int** |  | 
**generation** | **str** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.resource_pool_add_request import ResourcePoolAddRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcePoolAddRequest from a JSON string
resource_pool_add_request_instance = ResourcePoolAddRequest.from_json(json)
# print the JSON string representation of the object
print(ResourcePoolAddRequest.to_json())

# convert the object into a dict
resource_pool_add_request_dict = resource_pool_add_request_instance.to_dict()
# create an instance of ResourcePoolAddRequest from a dict
resource_pool_add_request_from_dict = ResourcePoolAddRequest.from_dict(resource_pool_add_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


