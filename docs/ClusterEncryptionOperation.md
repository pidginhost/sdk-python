# ClusterEncryptionOperation

One encryption change, as the customer sees it.  ``verification_result`` is deliberately absent: the evidence is published once, sanitised, as the state's ``per_node`` -- two copies of a JSON column are two places for key material to escape from.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**kind** | **str** |  | [readonly] 
**status** | **str** |  | [readonly] 
**requested_mode** | **str** |  | [readonly] 
**previous_mode** | **str** |  | [readonly] 
**reason** | **str** |  | [readonly] 
**message** | **str** |  | [readonly] 
**override_unverifiable** | **bool** |  | [readonly] 
**request_id** | **str** |  | [readonly] 
**created_at** | **str** |  | [readonly] 
**finished_at** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.cluster_encryption_operation import ClusterEncryptionOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterEncryptionOperation from a JSON string
cluster_encryption_operation_instance = ClusterEncryptionOperation.from_json(json)
# print the JSON string representation of the object
print(ClusterEncryptionOperation.to_json())

# convert the object into a dict
cluster_encryption_operation_dict = cluster_encryption_operation_instance.to_dict()
# create an instance of ClusterEncryptionOperation from a dict
cluster_encryption_operation_from_dict = ClusterEncryptionOperation.from_dict(cluster_encryption_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


