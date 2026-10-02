# ResourcePoolRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_size** | **int** |  | [optional] 
**local_data_loss_accepted** | **bool** |  | [optional] [default to False]

## Example

```python
from pidginhost_sdk.models.resource_pool_request import ResourcePoolRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcePoolRequest from a JSON string
resource_pool_request_instance = ResourcePoolRequest.from_json(json)
# print the JSON string representation of the object
print(ResourcePoolRequest.to_json())

# convert the object into a dict
resource_pool_request_dict = resource_pool_request_instance.to_dict()
# create an instance of ResourcePoolRequest from a dict
resource_pool_request_from_dict = ResourcePoolRequest.from_dict(resource_pool_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


