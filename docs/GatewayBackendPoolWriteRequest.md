# GatewayBackendPoolWriteRequest

The fields a customer writes; gateway.backend_pools.clean_pool decides what they may hold.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**policy** | [**GatewayBackendPoolPolicyEnum**](GatewayBackendPoolPolicyEnum.md) |  | [optional] 
**proxy_protocol** | **bool** | PROXY protocol v2 to the servers; tcp only. | [optional] 
**health_check** | [**GatewayHealthCheckWriteRequest**](GatewayHealthCheckWriteRequest.md) |  | [optional] 

## Example

```python
from pidginhost_sdk.models.gateway_backend_pool_write_request import GatewayBackendPoolWriteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayBackendPoolWriteRequest from a JSON string
gateway_backend_pool_write_request_instance = GatewayBackendPoolWriteRequest.from_json(json)
# print the JSON string representation of the object
print(GatewayBackendPoolWriteRequest.to_json())

# convert the object into a dict
gateway_backend_pool_write_request_dict = gateway_backend_pool_write_request_instance.to_dict()
# create an instance of GatewayBackendPoolWriteRequest from a dict
gateway_backend_pool_write_request_from_dict = GatewayBackendPoolWriteRequest.from_dict(gateway_backend_pool_write_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


