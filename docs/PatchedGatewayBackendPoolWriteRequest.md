# PatchedGatewayBackendPoolWriteRequest

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
from pidginhost_sdk.models.patched_gateway_backend_pool_write_request import PatchedGatewayBackendPoolWriteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedGatewayBackendPoolWriteRequest from a JSON string
patched_gateway_backend_pool_write_request_instance = PatchedGatewayBackendPoolWriteRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedGatewayBackendPoolWriteRequest.to_json())

# convert the object into a dict
patched_gateway_backend_pool_write_request_dict = patched_gateway_backend_pool_write_request_instance.to_dict()
# create an instance of PatchedGatewayBackendPoolWriteRequest from a dict
patched_gateway_backend_pool_write_request_from_dict = PatchedGatewayBackendPoolWriteRequest.from_dict(patched_gateway_backend_pool_write_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


