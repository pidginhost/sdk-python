# PaginatedDepositList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Deposit]**](Deposit.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_deposit_list import PaginatedDepositList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedDepositList from a JSON string
paginated_deposit_list_instance = PaginatedDepositList.from_json(json)
# print the JSON string representation of the object
print(PaginatedDepositList.to_json())

# convert the object into a dict
paginated_deposit_list_dict = paginated_deposit_list_instance.to_dict()
# create an instance of PaginatedDepositList from a dict
paginated_deposit_list_from_dict = PaginatedDepositList.from_dict(paginated_deposit_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


