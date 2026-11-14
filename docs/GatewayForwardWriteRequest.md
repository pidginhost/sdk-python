# GatewayForwardWriteRequest

The fields a customer writes; gateway.forwards.clean_forward decides what they may hold.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | [**GatewayForwardProtocolEnum**](GatewayForwardProtocolEnum.md) |  | 
**public_ports** | [**GatewayPortRangeRequest**](GatewayPortRangeRequest.md) |  | 
**target** | [**GatewayForwardTargetRequest**](GatewayForwardTargetRequest.md) |  | 
**allowed_sources** | **List[str]** | IPv4 networks; empty means any source. | [optional] 
**preserve_client_ip** | **bool** | Only false is accepted for now. | [optional] 
**enabled** | **bool** |  | [optional] 
**comment** | **str** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.gateway_forward_write_request import GatewayForwardWriteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayForwardWriteRequest from a JSON string
gateway_forward_write_request_instance = GatewayForwardWriteRequest.from_json(json)
# print the JSON string representation of the object
print(GatewayForwardWriteRequest.to_json())

# convert the object into a dict
gateway_forward_write_request_dict = gateway_forward_write_request_instance.to_dict()
# create an instance of GatewayForwardWriteRequest from a dict
gateway_forward_write_request_from_dict = GatewayForwardWriteRequest.from_dict(gateway_forward_write_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


