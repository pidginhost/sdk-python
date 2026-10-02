# PatchedTCPRouteRequest

Serializer for TCPRoute resources with port validation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**port** | **int** | External port to expose (blocked: 22, 6443, 50000, 50001) | [optional] 
**backend_service_name** | **str** | Name of the backend Kubernetes Service | [optional] 
**backend_service_port** | **int** | Port of the backend Service | [optional] 
**backend_namespace** | **str** | Namespace of the backend Service | [optional] [default to 'default']

## Example

```python
from pidginhost_sdk.models.patched_tcp_route_request import PatchedTCPRouteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedTCPRouteRequest from a JSON string
patched_tcp_route_request_instance = PatchedTCPRouteRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedTCPRouteRequest.to_json())

# convert the object into a dict
patched_tcp_route_request_dict = patched_tcp_route_request_instance.to_dict()
# create an instance of PatchedTCPRouteRequest from a dict
patched_tcp_route_request_from_dict = PatchedTCPRouteRequest.from_dict(patched_tcp_route_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


