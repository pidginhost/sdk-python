# PatchedGatewayForwardWriteRequest

The fields a customer writes; gateway.forwards.clean_forward decides what they may hold.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | [**GatewayForwardProtocolEnum**](GatewayForwardProtocolEnum.md) |  | [optional] 
**public_ports** | [**GatewayPortRangeRequest**](GatewayPortRangeRequest.md) |  | [optional] 
**target** | [**GatewayForwardTargetRequest**](GatewayForwardTargetRequest.md) |  | [optional] 
**allowed_sources** | **List[str]** | IPv4 networks; empty means any source. | [optional] 
**preserve_client_ip** | **bool** | Only false is accepted for now. | [optional] 
**enabled** | **bool** |  | [optional] 
**comment** | **str** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.patched_gateway_forward_write_request import PatchedGatewayForwardWriteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedGatewayForwardWriteRequest from a JSON string
patched_gateway_forward_write_request_instance = PatchedGatewayForwardWriteRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedGatewayForwardWriteRequest.to_json())

# convert the object into a dict
patched_gateway_forward_write_request_dict = patched_gateway_forward_write_request_instance.to_dict()
# create an instance of PatchedGatewayForwardWriteRequest from a dict
patched_gateway_forward_write_request_from_dict = PatchedGatewayForwardWriteRequest.from_dict(patched_gateway_forward_write_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


