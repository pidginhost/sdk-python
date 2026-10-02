# PowerActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**PowerActionActionEnum**](PowerActionActionEnum.md) |  | 

## Example

```python
from pidginhost_sdk.models.power_action_request import PowerActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PowerActionRequest from a JSON string
power_action_request_instance = PowerActionRequest.from_json(json)
# print the JSON string representation of the object
print(PowerActionRequest.to_json())

# convert the object into a dict
power_action_request_dict = power_action_request_instance.to_dict()
# create an instance of PowerActionRequest from a dict
power_action_request_from_dict = PowerActionRequest.from_dict(power_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


