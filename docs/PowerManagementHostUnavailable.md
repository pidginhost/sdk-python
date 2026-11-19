# PowerManagementHostUnavailable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.power_management_host_unavailable import PowerManagementHostUnavailable

# TODO update the JSON string below
json = "{}"
# create an instance of PowerManagementHostUnavailable from a JSON string
power_management_host_unavailable_instance = PowerManagementHostUnavailable.from_json(json)
# print the JSON string representation of the object
print(PowerManagementHostUnavailable.to_json())

# convert the object into a dict
power_management_host_unavailable_dict = power_management_host_unavailable_instance.to_dict()
# create an instance of PowerManagementHostUnavailable from a dict
power_management_host_unavailable_from_dict = PowerManagementHostUnavailable.from_dict(power_management_host_unavailable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


