# GatewayLBListener

A load balancer listener (spec 6.8): one public port with a mode; pending until applied.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**protocol** | [**GatewayForwardProtocolEnum**](GatewayForwardProtocolEnum.md) |  | [readonly] 
**port** | **int** |  | 
**mode** | [**GatewayLBListenerModeEnum**](GatewayLBListenerModeEnum.md) |  | 
**pool** | **int** | The backend pool of a tcp or udp listener; null for http. | 
**allowed_sources** | **List[str]** | Empty means any source. | 
**enabled** | **bool** |  | [readonly] 
**comment** | **str** |  | [readonly] 
**changed_revision** | **int** |  | [readonly] 
**pending** | **bool** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.gateway_lb_listener import GatewayLBListener

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayLBListener from a JSON string
gateway_lb_listener_instance = GatewayLBListener.from_json(json)
# print the JSON string representation of the object
print(GatewayLBListener.to_json())

# convert the object into a dict
gateway_lb_listener_dict = gateway_lb_listener_instance.to_dict()
# create an instance of GatewayLBListener from a dict
gateway_lb_listener_from_dict = GatewayLBListener.from_dict(gateway_lb_listener_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


