# GatewayRouteWriteRequest

The fields a customer writes; gateway.lb_routes.clean_route decides what they may hold.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostnames** | **List[str]** | Up to 16 names; empty matches every host. | [optional] 
**path_prefix** | **str** | Literal and case-sensitive. | [optional] 
**pool** | **int** | A backend pool&#39;s id. | [optional] 
**redirect_https** | **bool** | Only false is accepted for now. | [optional] 
**enabled** | **bool** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.gateway_route_write_request import GatewayRouteWriteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayRouteWriteRequest from a JSON string
gateway_route_write_request_instance = GatewayRouteWriteRequest.from_json(json)
# print the JSON string representation of the object
print(GatewayRouteWriteRequest.to_json())

# convert the object into a dict
gateway_route_write_request_dict = gateway_route_write_request_instance.to_dict()
# create an instance of GatewayRouteWriteRequest from a dict
gateway_route_write_request_from_dict = GatewayRouteWriteRequest.from_dict(gateway_route_write_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


