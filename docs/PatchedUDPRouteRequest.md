# PatchedUDPRouteRequest

Serializer for UDPRoute resources with port validation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**port** | **int** | External port to expose | [optional] 
**backend_service_name** | **str** | Name of the backend Kubernetes Service | [optional] 
**backend_service_port** | **int** | Port of the backend Service | [optional] 
**backend_namespace** | **str** | Namespace of the backend Service | [optional] [default to 'default']

## Example

```python
from pidginhost_sdk.models.patched_udp_route_request import PatchedUDPRouteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedUDPRouteRequest from a JSON string
patched_udp_route_request_instance = PatchedUDPRouteRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedUDPRouteRequest.to_json())

# convert the object into a dict
patched_udp_route_request_dict = patched_udp_route_request_instance.to_dict()
# create an instance of PatchedUDPRouteRequest from a dict
patched_udp_route_request_from_dict = PatchedUDPRouteRequest.from_dict(patched_udp_route_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


