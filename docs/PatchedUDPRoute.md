# PatchedUDPRoute

Serializer for UDPRoute resources with port validation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**port** | **int** | External port to expose | [optional] 
**backend_service_name** | **str** | Name of the backend Kubernetes Service | [optional] 
**backend_service_port** | **int** | Port of the backend Service | [optional] 
**backend_namespace** | **str** | Namespace of the backend Service | [optional] [default to 'default']
**status_ready** | **bool** |  | [optional] [readonly] 
**status_message** | **str** |  | [optional] [readonly] 
**created** | **str** |  | [optional] [readonly] 
**updated** | **str** |  | [optional] [readonly] 

## Example

```python
from pidginhost_sdk.models.patched_udp_route import PatchedUDPRoute

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedUDPRoute from a JSON string
patched_udp_route_instance = PatchedUDPRoute.from_json(json)
# print the JSON string representation of the object
print(PatchedUDPRoute.to_json())

# convert the object into a dict
patched_udp_route_dict = patched_udp_route_instance.to_dict()
# create an instance of PatchedUDPRoute from a dict
patched_udp_route_from_dict = PatchedUDPRoute.from_dict(patched_udp_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


