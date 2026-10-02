# ClusterEncryptionError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**reason** | [**EncryptionReasonCodeEnum**](EncryptionReasonCodeEnum.md) |  | [optional] 
**extra** | **Dict[str, object]** |  | [optional] 
**code** | **str** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.cluster_encryption_error import ClusterEncryptionError

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterEncryptionError from a JSON string
cluster_encryption_error_instance = ClusterEncryptionError.from_json(json)
# print the JSON string representation of the object
print(ClusterEncryptionError.to_json())

# convert the object into a dict
cluster_encryption_error_dict = cluster_encryption_error_instance.to_dict()
# create an instance of ClusterEncryptionError from a dict
cluster_encryption_error_from_dict = ClusterEncryptionError.from_dict(cluster_encryption_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


