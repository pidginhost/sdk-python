# PaginatedEmailHistoryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[EmailHistory]**](EmailHistory.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_email_history_list import PaginatedEmailHistoryList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedEmailHistoryList from a JSON string
paginated_email_history_list_instance = PaginatedEmailHistoryList.from_json(json)
# print the JSON string representation of the object
print(PaginatedEmailHistoryList.to_json())

# convert the object into a dict
paginated_email_history_list_dict = paginated_email_history_list_instance.to_dict()
# create an instance of PaginatedEmailHistoryList from a dict
paginated_email_history_list_from_dict = PaginatedEmailHistoryList.from_dict(paginated_email_history_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


