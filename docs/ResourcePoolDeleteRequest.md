# ResourcePoolDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_data_loss_accepted** | **bool** | Acknowledge that data kept on the pool&#39;s nodes is destroyed. Not needed for an empty pool. | [optional] [default to False]

## Example

```python
from pidginhost_sdk.models.resource_pool_delete_request import ResourcePoolDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcePoolDeleteRequest from a JSON string
resource_pool_delete_request_instance = ResourcePoolDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(ResourcePoolDeleteRequest.to_json())

# convert the object into a dict
resource_pool_delete_request_dict = resource_pool_delete_request_instance.to_dict()
# create an instance of ResourcePoolDeleteRequest from a dict
resource_pool_delete_request_from_dict = ResourcePoolDeleteRequest.from_dict(resource_pool_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


