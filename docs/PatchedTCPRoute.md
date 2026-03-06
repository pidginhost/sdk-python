# PatchedTCPRoute

Serializer for TCPRoute resources with port validation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**port** | **int** | External port to expose (blocked: 22, 6443, 50000, 50001) | [optional] 
**backend_service_name** | **str** | Name of the backend Kubernetes Service | [optional] 
**backend_service_port** | **int** | Port of the backend Service | [optional] 
**backend_namespace** | **str** | Namespace of the backend Service | [optional] [default to 'default']
**status_ready** | **bool** |  | [optional] [readonly] 
**status_message** | **str** |  | [optional] [readonly] 
**created** | **str** |  | [optional] [readonly] 
**updated** | **str** |  | [optional] [readonly] 

## Example

```python
from pidginhost_sdk.models.patched_tcp_route import PatchedTCPRoute

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedTCPRoute from a JSON string
patched_tcp_route_instance = PatchedTCPRoute.from_json(json)
# print the JSON string representation of the object
print(PatchedTCPRoute.to_json())

# convert the object into a dict
patched_tcp_route_dict = patched_tcp_route_instance.to_dict()
# create an instance of PatchedTCPRoute from a dict
patched_tcp_route_from_dict = PatchedTCPRoute.from_dict(patched_tcp_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


