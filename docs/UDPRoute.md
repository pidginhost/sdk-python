# UDPRoute

Serializer for UDPRoute resources with port validation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**namespace** | **str** |  | [optional] 
**port** | **int** | External port to expose | 
**backend_service_name** | **str** | Name of the backend Kubernetes Service | 
**backend_service_port** | **int** | Port of the backend Service | 
**backend_namespace** | **str** | Namespace of the backend Service | [optional] [default to 'default']
**status_ready** | **bool** |  | [readonly] 
**status_message** | **str** |  | [readonly] 
**created** | **str** |  | [readonly] 
**updated** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.udp_route import UDPRoute

# TODO update the JSON string below
json = "{}"
# create an instance of UDPRoute from a JSON string
udp_route_instance = UDPRoute.from_json(json)
# print the JSON string representation of the object
print(UDPRoute.to_json())

# convert the object into a dict
udp_route_dict = udp_route_instance.to_dict()
# create an instance of UDPRoute from a dict
udp_route_from_dict = UDPRoute.from_dict(udp_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


