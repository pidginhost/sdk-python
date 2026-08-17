# LowBalanceSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threshold_type** | [**ThresholdTypeEnum**](ThresholdTypeEnum.md) |  | 
**threshold_amount** | **decimal.Decimal** |  | [optional] 
**threshold_days** | **int** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.low_balance_settings import LowBalanceSettings

# TODO update the JSON string below
json = "{}"
# create an instance of LowBalanceSettings from a JSON string
low_balance_settings_instance = LowBalanceSettings.from_json(json)
# print the JSON string representation of the object
print(LowBalanceSettings.to_json())

# convert the object into a dict
low_balance_settings_dict = low_balance_settings_instance.to_dict()
# create an instance of LowBalanceSettings from a dict
low_balance_settings_from_dict = LowBalanceSettings.from_dict(low_balance_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


