# PatchedGatewayUpdateRequest

The name, and the maintenance window: weekday 0 (Monday) to 6 (Sunday), hour 0 to 23, Bucharest time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**maintenance_weekday** | **int** |  | [optional] 
**maintenance_hour** | **int** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.patched_gateway_update_request import PatchedGatewayUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedGatewayUpdateRequest from a JSON string
patched_gateway_update_request_instance = PatchedGatewayUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedGatewayUpdateRequest.to_json())

# convert the object into a dict
patched_gateway_update_request_dict = patched_gateway_update_request_instance.to_dict()
# create an instance of PatchedGatewayUpdateRequest from a dict
patched_gateway_update_request_from_dict = PatchedGatewayUpdateRequest.from_dict(patched_gateway_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


