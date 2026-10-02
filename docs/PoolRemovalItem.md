# PoolRemovalItem

One worker a journal is removing, and how far its removal got.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_hostname** | **str** |  | [readonly] 
**cordoned_at** | **str** |  | [readonly] 
**drained_at** | **str** |  | [readonly] 
**detached_at** | **str** |  | [readonly] 
**validated_at** | **str** |  | [readonly] 
**reset_started_at** | **str** |  | [readonly] 
**reset_completed_at** | **str** |  | [readonly] 
**node_deleted_at** | **str** |  | [readonly] 
**vm_deleted_at** | **str** |  | [readonly] 
**uncordoned_at** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.pool_removal_item import PoolRemovalItem

# TODO update the JSON string below
json = "{}"
# create an instance of PoolRemovalItem from a JSON string
pool_removal_item_instance = PoolRemovalItem.from_json(json)
# print the JSON string representation of the object
print(PoolRemovalItem.to_json())

# convert the object into a dict
pool_removal_item_dict = pool_removal_item_instance.to_dict()
# create an instance of PoolRemovalItem from a dict
pool_removal_item_from_dict = PoolRemovalItem.from_dict(pool_removal_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


