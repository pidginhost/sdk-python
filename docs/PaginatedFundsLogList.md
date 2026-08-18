# PaginatedFundsLogList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[FundsLog]**](FundsLog.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_funds_log_list import PaginatedFundsLogList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedFundsLogList from a JSON string
paginated_funds_log_list_instance = PaginatedFundsLogList.from_json(json)
# print the JSON string representation of the object
print(PaginatedFundsLogList.to_json())

# convert the object into a dict
paginated_funds_log_list_dict = paginated_funds_log_list_instance.to_dict()
# create an instance of PaginatedFundsLogList from a dict
paginated_funds_log_list_from_dict = PaginatedFundsLogList.from_dict(paginated_funds_log_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


