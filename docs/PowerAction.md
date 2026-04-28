# PowerAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**PowerActionActionEnum**](PowerActionActionEnum.md) |  | 

## Example

```python
from pidginhost_sdk.models.power_action import PowerAction

# TODO update the JSON string below
json = "{}"
# create an instance of PowerAction from a JSON string
power_action_instance = PowerAction.from_json(json)
# print the JSON string representation of the object
print(PowerAction.to_json())

# convert the object into a dict
power_action_dict = power_action_instance.to_dict()
# create an instance of PowerAction from a dict
power_action_from_dict = PowerAction.from_dict(power_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


