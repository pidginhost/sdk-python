# PaginatedSnapshotList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Snapshot]**](Snapshot.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_snapshot_list import PaginatedSnapshotList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSnapshotList from a JSON string
paginated_snapshot_list_instance = PaginatedSnapshotList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSnapshotList.to_json())

# convert the object into a dict
paginated_snapshot_list_dict = paginated_snapshot_list_instance.to_dict()
# create an instance of PaginatedSnapshotList from a dict
paginated_snapshot_list_from_dict = PaginatedSnapshotList.from_dict(paginated_snapshot_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


