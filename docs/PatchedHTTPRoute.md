# PatchedHTTPRoute

Serializer for HTTPRoute resources with automatic certificate issuance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**hostnames** | **List[str]** | List of hostnames to route (e.g., [\&quot;example.com\&quot;, \&quot;www.example.com\&quot;]) | [optional] 
**backend_service_name** | **str** | Name of the backend Kubernetes Service | [optional] 
**backend_service_port** | **int** | Port of the backend Service | [optional] 
**backend_namespace** | **str** | Namespace of the backend Service | [optional] [default to 'default']
**path_prefix** | **str** | Path prefix to match (default: /) | [optional] [default to '/']
**enable_tls** | **bool** | Enable TLS termination with automatic certificate issuance | [optional] [default to True]
**status_ready** | **bool** |  | [optional] [readonly] 
**status_message** | **str** |  | [optional] [readonly] 
**created** | **str** |  | [optional] [readonly] 
**updated** | **str** |  | [optional] [readonly] 

## Example

```python
from pidginhost_sdk.models.patched_http_route import PatchedHTTPRoute

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedHTTPRoute from a JSON string
patched_http_route_instance = PatchedHTTPRoute.from_json(json)
# print the JSON string representation of the object
print(PatchedHTTPRoute.to_json())

# convert the object into a dict
patched_http_route_dict = patched_http_route_instance.to_dict()
# create an instance of PatchedHTTPRoute from a dict
patched_http_route_from_dict = PatchedHTTPRoute.from_dict(patched_http_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


