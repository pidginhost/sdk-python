# GatewayLBListenerWriteRequest

The fields a customer writes; gateway.lb_listeners.clean_listener decides what they may hold.  protocol, port and mode are set at creation and cannot change.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | [**GatewayForwardProtocolEnum**](GatewayForwardProtocolEnum.md) |  | [optional] 
**port** | **int** |  | [optional] 
**mode** | [**GatewayLBListenerModeEnum**](GatewayLBListenerModeEnum.md) | tcp, udp or http; https is not available yet.  * &#x60;tcp&#x60; - tcp * &#x60;udp&#x60; - udp * &#x60;http&#x60; - http * &#x60;https&#x60; - https | [optional] 
**pool** | **int** | A backend pool&#39;s id; tcp and udp only. | [optional] 
**allowed_sources** | **List[str]** | IPv4 and IPv6 networks; empty means any source. | [optional] 
**enabled** | **bool** |  | [optional] 
**comment** | **str** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.gateway_lb_listener_write_request import GatewayLBListenerWriteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayLBListenerWriteRequest from a JSON string
gateway_lb_listener_write_request_instance = GatewayLBListenerWriteRequest.from_json(json)
# print the JSON string representation of the object
print(GatewayLBListenerWriteRequest.to_json())

# convert the object into a dict
gateway_lb_listener_write_request_dict = gateway_lb_listener_write_request_instance.to_dict()
# create an instance of GatewayLBListenerWriteRequest from a dict
gateway_lb_listener_write_request_from_dict = GatewayLBListenerWriteRequest.from_dict(gateway_lb_listener_write_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


