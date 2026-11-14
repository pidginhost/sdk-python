# GatewayBackend

A pool's server (spec 5.5) with its health as the gateway last reported it (spec 6.8).  The view passes the health map in the context, read once per request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**network** | **int** | An attached private network&#39;s id. | 
**address** | **str** |  | [readonly] 
**port** | **int** |  | [readonly] 
**weight** | **int** |  | [readonly] 
**enabled** | **bool** |  | [readonly] 
**health** | [**GatewayBackendHealthEnum**](GatewayBackendHealthEnum.md) |  | [readonly] 
**health_changed** | **str** |  | [readonly] 
**changed_revision** | **int** |  | [readonly] 
**pending** | **bool** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.gateway_backend import GatewayBackend

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayBackend from a JSON string
gateway_backend_instance = GatewayBackend.from_json(json)
# print the JSON string representation of the object
print(GatewayBackend.to_json())

# convert the object into a dict
gateway_backend_dict = gateway_backend_instance.to_dict()
# create an instance of GatewayBackend from a dict
gateway_backend_from_dict = GatewayBackend.from_dict(gateway_backend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


