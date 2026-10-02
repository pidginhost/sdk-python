# ClusterEncryptionRefusal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | [**EncryptionReasonCodeEnum**](EncryptionReasonCodeEnum.md) |  | 
**message** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.cluster_encryption_refusal import ClusterEncryptionRefusal

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterEncryptionRefusal from a JSON string
cluster_encryption_refusal_instance = ClusterEncryptionRefusal.from_json(json)
# print the JSON string representation of the object
print(ClusterEncryptionRefusal.to_json())

# convert the object into a dict
cluster_encryption_refusal_dict = cluster_encryption_refusal_instance.to_dict()
# create an instance of ClusterEncryptionRefusal from a dict
cluster_encryption_refusal_from_dict = ClusterEncryptionRefusal.from_dict(cluster_encryption_refusal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


