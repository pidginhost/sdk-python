# FundsBalanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **decimal.Decimal** |  | 
**threshold_type** | **str** |  | 
**threshold_amount** | **decimal.Decimal** |  | 
**threshold_days** | **int** |  | 

## Example

```python
from pidginhost_sdk.models.funds_balance_response import FundsBalanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FundsBalanceResponse from a JSON string
funds_balance_response_instance = FundsBalanceResponse.from_json(json)
# print the JSON string representation of the object
print(FundsBalanceResponse.to_json())

# convert the object into a dict
funds_balance_response_dict = funds_balance_response_instance.to_dict()
# create an instance of FundsBalanceResponse from a dict
funds_balance_response_from_dict = FundsBalanceResponse.from_dict(funds_balance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


