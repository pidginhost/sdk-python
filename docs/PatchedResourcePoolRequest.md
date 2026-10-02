# PatchedResourcePoolRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_size** | **int** |  | [optional] 
**local_data_loss_accepted** | **bool** |  | [optional] [default to False]

## Example

```python
from pidginhost_sdk.models.patched_resource_pool_request import PatchedResourcePoolRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedResourcePoolRequest from a JSON string
patched_resource_pool_request_instance = PatchedResourcePoolRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedResourcePoolRequest.to_json())

# convert the object into a dict
patched_resource_pool_request_dict = patched_resource_pool_request_instance.to_dict()
# create an instance of PatchedResourcePoolRequest from a dict
patched_resource_pool_request_from_dict = PatchedResourcePoolRequest.from_dict(patched_resource_pool_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


