# FundsLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**var_date** | **str** |  | [readonly] 
**operation** | [**OperationEnum**](OperationEnum.md) |  | [readonly] 
**amount** | **str** | + or - sum | [readonly] 
**balance** | **str** | Balance after operation | [readonly] 
**for_date** | **date** | Used for cloud service payments | [readonly] 

## Example

```python
from pidginhost_sdk.models.funds_log import FundsLog

# TODO update the JSON string below
json = "{}"
# create an instance of FundsLog from a JSON string
funds_log_instance = FundsLog.from_json(json)
# print the JSON string representation of the object
print(FundsLog.to_json())

# convert the object into a dict
funds_log_dict = funds_log_instance.to_dict()
# create an instance of FundsLog from a dict
funds_log_from_dict = FundsLog.from_dict(funds_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


