# PoolRemovalJournal

What a customer may see about a downsize or pool deletion.  There is no `source` here and the row records none. The spec's \"pool journals apply the same split\" is about the customer/staff partition, not a field-for-field mirror of the node operation: a journal's initiator is already `actor_label`, and a `source` column would have to be threaded through four call sites to say something no reader distinguishes. The day a `source=\"system\"` caller exists it becomes an additive `AddField`; until then it would be a column nothing can populate truthfully.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**kind** | [**PoolRemovalJournalKindEnum**](PoolRemovalJournalKindEnum.md) |  | [readonly] 
**status** | [**PoolRemovalJournalStatusEnum**](PoolRemovalJournalStatusEnum.md) |  | [readonly] 
**reason** | **str** |  | [readonly] 
**message** | **str** |  | [readonly] 
**requested_pool_size** | **int** |  | [readonly] 
**local_data_loss_accepted** | **bool** |  | [readonly] 
**actor_label** | **str** | Who requested the removal (user email or staff name). Never token material. | [readonly] 
**created_at** | **str** |  | [readonly] 
**updated_at** | **str** |  | [readonly] 
**finished_at** | **str** |  | [readonly] 
**items** | [**List[PoolRemovalItem]**](PoolRemovalItem.md) |  | [readonly] 
**allowed_actions** | **List[str]** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.pool_removal_journal import PoolRemovalJournal

# TODO update the JSON string below
json = "{}"
# create an instance of PoolRemovalJournal from a JSON string
pool_removal_journal_instance = PoolRemovalJournal.from_json(json)
# print the JSON string representation of the object
print(PoolRemovalJournal.to_json())

# convert the object into a dict
pool_removal_journal_dict = pool_removal_journal_instance.to_dict()
# create an instance of PoolRemovalJournal from a dict
pool_removal_journal_from_dict = PoolRemovalJournal.from_dict(pool_removal_journal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


