# GatewayHealthCheckWriteRequest

The check fields a customer writes; a missing one keeps its value, and a type takes only its own fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**GatewayHealthCheckTypeEnum**](GatewayHealthCheckTypeEnum.md) |  | [optional] 
**path** | **str** | http only. | [optional] 
**status_min** | **int** | http only. | [optional] 
**status_max** | **int** | http only. | [optional] 
**interval_s** | **int** |  | [optional] 
**timeout_s** | **int** | Below interval_s. | [optional] 
**healthy_threshold** | **int** |  | [optional] 
**unhealthy_threshold** | **int** |  | [optional] 
**port** | **int** | Null checks each server&#39;s own port. | [optional] 

## Example

```python
from pidginhost_sdk.models.gateway_health_check_write_request import GatewayHealthCheckWriteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayHealthCheckWriteRequest from a JSON string
gateway_health_check_write_request_instance = GatewayHealthCheckWriteRequest.from_json(json)
# print the JSON string representation of the object
print(GatewayHealthCheckWriteRequest.to_json())

# convert the object into a dict
gateway_health_check_write_request_dict = gateway_health_check_write_request_instance.to_dict()
# create an instance of GatewayHealthCheckWriteRequest from a dict
gateway_health_check_write_request_from_dict = GatewayHealthCheckWriteRequest.from_dict(gateway_health_check_write_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


