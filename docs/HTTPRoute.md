# HTTPRoute

Serializer for HTTPRoute resources with automatic certificate issuance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**namespace** | **str** |  | [optional] 
**hostnames** | **List[str]** | List of hostnames to route (e.g., [\&quot;example.com\&quot;, \&quot;www.example.com\&quot;]) | 
**backend_service_name** | **str** | Name of the backend Kubernetes Service | 
**backend_service_port** | **int** | Port of the backend Service | 
**backend_namespace** | **str** | Namespace of the backend Service | [optional] [default to 'default']
**path_prefix** | **str** | Path prefix to match (default: /) | [optional] [default to '/']
**enable_tls** | **bool** | Enable TLS termination with automatic certificate issuance | [optional] [default to True]
**status_ready** | **bool** |  | [readonly] 
**status_message** | **str** |  | [readonly] 
**created** | **str** |  | [readonly] 
**updated** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.http_route import HTTPRoute

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPRoute from a JSON string
http_route_instance = HTTPRoute.from_json(json)
# print the JSON string representation of the object
print(HTTPRoute.to_json())

# convert the object into a dict
http_route_dict = http_route_instance.to_dict()
# create an instance of HTTPRoute from a dict
http_route_from_dict = HTTPRoute.from_dict(http_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


