# PaginatedSuppressionEntryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[SuppressionEntry]**](SuppressionEntry.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_suppression_entry_list import PaginatedSuppressionEntryList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSuppressionEntryList from a JSON string
paginated_suppression_entry_list_instance = PaginatedSuppressionEntryList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSuppressionEntryList.to_json())

# convert the object into a dict
paginated_suppression_entry_list_dict = paginated_suppression_entry_list_instance.to_dict()
# create an instance of PaginatedSuppressionEntryList from a dict
paginated_suppression_entry_list_from_dict = PaginatedSuppressionEntryList.from_dict(paginated_suppression_entry_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


