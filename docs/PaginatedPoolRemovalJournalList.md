# PaginatedPoolRemovalJournalList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PoolRemovalJournal]**](PoolRemovalJournal.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_pool_removal_journal_list import PaginatedPoolRemovalJournalList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPoolRemovalJournalList from a JSON string
paginated_pool_removal_journal_list_instance = PaginatedPoolRemovalJournalList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPoolRemovalJournalList.to_json())

# convert the object into a dict
paginated_pool_removal_journal_list_dict = paginated_pool_removal_journal_list_instance.to_dict()
# create an instance of PaginatedPoolRemovalJournalList from a dict
paginated_pool_removal_journal_list_from_dict = PaginatedPoolRemovalJournalList.from_dict(paginated_pool_removal_journal_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


