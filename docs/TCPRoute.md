# TCPRoute

Serializer for TCPRoute resources with port validation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**namespace** | **str** |  | [optional] 
**port** | **int** | External port to expose (blocked: 22, 6443, 50000, 50001) | 
**backend_service_name** | **str** | Name of the backend Kubernetes Service | 
**backend_service_port** | **int** | Port of the backend Service | 
**backend_namespace** | **str** | Namespace of the backend Service | [optional] [default to 'default']
**status_ready** | **bool** |  | [readonly] 
**status_message** | **str** |  | [readonly] 
**created** | **str** |  | [readonly] 
**updated** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.tcp_route import TCPRoute

# TODO update the JSON string below
json = "{}"
# create an instance of TCPRoute from a JSON string
tcp_route_instance = TCPRoute.from_json(json)
# print the JSON string representation of the object
print(TCPRoute.to_json())

# convert the object into a dict
tcp_route_dict = tcp_route_instance.to_dict()
# create an instance of TCPRoute from a dict
tcp_route_from_dict = TCPRoute.from_dict(tcp_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


