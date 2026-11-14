# GatewayBackendPool

A backend pool (spec 5.5): the servers a listener or route sends to; pending until applied.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | [readonly] 
**policy** | [**GatewayBackendPoolPolicyEnum**](GatewayBackendPoolPolicyEnum.md) |  | [readonly] 
**proxy_protocol** | **bool** |  | [readonly] 
**health_check** | [**GatewayHealthCheck**](GatewayHealthCheck.md) |  | [readonly] 
**changed_revision** | **int** |  | [readonly] 
**pending** | **bool** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.gateway_backend_pool import GatewayBackendPool

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayBackendPool from a JSON string
gateway_backend_pool_instance = GatewayBackendPool.from_json(json)
# print the JSON string representation of the object
print(GatewayBackendPool.to_json())

# convert the object into a dict
gateway_backend_pool_dict = gateway_backend_pool_instance.to_dict()
# create an instance of GatewayBackendPool from a dict
gateway_backend_pool_from_dict = GatewayBackendPool.from_dict(gateway_backend_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


