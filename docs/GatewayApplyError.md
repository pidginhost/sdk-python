# GatewayApplyError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | The kind of the object the agent refused, or null. | 
**id** | **int** |  | 
**message** | **str** |  | 
**rollback** | **str** | not_needed, pending, succeeded or failed. | 

## Example

```python
from pidginhost_sdk.models.gateway_apply_error import GatewayApplyError

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayApplyError from a JSON string
gateway_apply_error_instance = GatewayApplyError.from_json(json)
# print the JSON string representation of the object
print(GatewayApplyError.to_json())

# convert the object into a dict
gateway_apply_error_dict = gateway_apply_error_instance.to_dict()
# create an instance of GatewayApplyError from a dict
gateway_apply_error_from_dict = GatewayApplyError.from_dict(gateway_apply_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


