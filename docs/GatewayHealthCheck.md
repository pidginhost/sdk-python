# GatewayHealthCheck

A pool's health check (spec 5.5); the fields its type does not have are null.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**GatewayHealthCheckTypeEnum**](GatewayHealthCheckTypeEnum.md) |  | 
**path** | **str** |  | 
**status_min** | **int** |  | 
**status_max** | **int** |  | 
**interval_s** | **int** |  | 
**timeout_s** | **int** |  | 
**healthy_threshold** | **int** |  | 
**unhealthy_threshold** | **int** |  | 
**port** | **int** | Null checks each server&#39;s own port. | 

## Example

```python
from pidginhost_sdk.models.gateway_health_check import GatewayHealthCheck

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayHealthCheck from a JSON string
gateway_health_check_instance = GatewayHealthCheck.from_json(json)
# print the JSON string representation of the object
print(GatewayHealthCheck.to_json())

# convert the object into a dict
gateway_health_check_dict = gateway_health_check_instance.to_dict()
# create an instance of GatewayHealthCheck from a dict
gateway_health_check_from_dict = GatewayHealthCheck.from_dict(gateway_health_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


