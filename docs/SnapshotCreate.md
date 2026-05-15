# SnapshotCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Letters, numbers, \&quot;.\&quot;, \&quot;_\&quot; and \&quot;-\&quot; (max 63 characters). | 
**description** | **str** |  | [optional] 
**include_memory** | **bool** |  | [optional] [default to False]

## Example

```python
from pidginhost_sdk.models.snapshot_create import SnapshotCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotCreate from a JSON string
snapshot_create_instance = SnapshotCreate.from_json(json)
# print the JSON string representation of the object
print(SnapshotCreate.to_json())

# convert the object into a dict
snapshot_create_dict = snapshot_create_instance.to_dict()
# create an instance of SnapshotCreate from a dict
snapshot_create_from_dict = SnapshotCreate.from_dict(snapshot_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


