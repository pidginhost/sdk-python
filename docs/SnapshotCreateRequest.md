# SnapshotCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Must start with a letter; letters, numbers, \&quot;_\&quot; and \&quot;-\&quot; only (2-40 characters). | 
**description** | **str** |  | [optional] 
**include_memory** | **bool** |  | [optional] [default to False]

## Example

```python
from pidginhost_sdk.models.snapshot_create_request import SnapshotCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotCreateRequest from a JSON string
snapshot_create_request_instance = SnapshotCreateRequest.from_json(json)
# print the JSON string representation of the object
print(SnapshotCreateRequest.to_json())

# convert the object into a dict
snapshot_create_request_dict = snapshot_create_request_instance.to_dict()
# create an instance of SnapshotCreateRequest from a dict
snapshot_create_request_from_dict = SnapshotCreateRequest.from_dict(snapshot_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


