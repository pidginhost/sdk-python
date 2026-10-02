# LowBalanceSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threshold_type** | [**ThresholdTypeEnum**](ThresholdTypeEnum.md) |  | 
**threshold_amount** | **decimal.Decimal** |  | [optional] 
**threshold_days** | **int** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.low_balance_settings_request import LowBalanceSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LowBalanceSettingsRequest from a JSON string
low_balance_settings_request_instance = LowBalanceSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(LowBalanceSettingsRequest.to_json())

# convert the object into a dict
low_balance_settings_request_dict = low_balance_settings_request_instance.to_dict()
# create an instance of LowBalanceSettingsRequest from a dict
low_balance_settings_request_from_dict = LowBalanceSettingsRequest.from_dict(low_balance_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


