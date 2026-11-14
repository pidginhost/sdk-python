# GatewayForward

A port forward (spec 6.7): public ports to one host of an attached network; pending until applied.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**protocol** | [**GatewayForwardProtocolEnum**](GatewayForwardProtocolEnum.md) |  | [readonly] 
**public_ports** | [**GatewayPortRange**](GatewayPortRange.md) |  | [readonly] 
**allowed_sources** | **object** |  | [readonly] 
**target** | [**GatewayForwardTarget**](GatewayForwardTarget.md) |  | [readonly] 
**preserve_client_ip** | **bool** | Always false: the target sees the gateway&#39;s address. | [readonly] 
**enabled** | **bool** |  | [readonly] 
**comment** | **str** |  | [readonly] 
**changed_revision** | **int** |  | [readonly] 
**pending** | **bool** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.gateway_forward import GatewayForward

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayForward from a JSON string
gateway_forward_instance = GatewayForward.from_json(json)
# print the JSON string representation of the object
print(GatewayForward.to_json())

# convert the object into a dict
gateway_forward_dict = gateway_forward_instance.to_dict()
# create an instance of GatewayForward from a dict
gateway_forward_from_dict = GatewayForward.from_dict(gateway_forward_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


