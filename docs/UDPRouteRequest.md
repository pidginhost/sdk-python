# UDPRouteRequest

Serializer for UDPRoute resources with port validation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**namespace** | **str** |  | [optional] 
**port** | **int** | External port to expose | 
**backend_service_name** | **str** | Name of the backend Kubernetes Service | 
**backend_service_port** | **int** | Port of the backend Service | 
**backend_namespace** | **str** | Namespace of the backend Service | [optional] [default to 'default']

## Example

```python
from pidginhost_sdk.models.udp_route_request import UDPRouteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UDPRouteRequest from a JSON string
udp_route_request_instance = UDPRouteRequest.from_json(json)
# print the JSON string representation of the object
print(UDPRouteRequest.to_json())

# convert the object into a dict
udp_route_request_dict = udp_route_request_instance.to_dict()
# create an instance of UDPRouteRequest from a dict
udp_route_request_from_dict = UDPRouteRequest.from_dict(udp_route_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


