# PowerManagementRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**PowerManagementRequestActionEnum**](PowerManagementRequestActionEnum.md) |  | 

## Example

```python
from pidginhost_sdk.models.power_management_request import PowerManagementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PowerManagementRequest from a JSON string
power_management_request_instance = PowerManagementRequest.from_json(json)
# print the JSON string representation of the object
print(PowerManagementRequest.to_json())

# convert the object into a dict
power_management_request_dict = power_management_request_instance.to_dict()
# create an instance of PowerManagementRequest from a dict
power_management_request_from_dict = PowerManagementRequest.from_dict(power_management_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


