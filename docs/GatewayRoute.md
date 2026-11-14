# GatewayRoute

An http listener's route (spec 5.6): a host and path prefix to a backend pool; pending until applied.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**hostnames** | **List[str]** | Empty matches every host. | 
**path_prefix** | **str** |  | [readonly] 
**pool** | **int** |  | 
**redirect_https** | **bool** | Always false: HTTPS redirects are not available yet. | [readonly] 
**enabled** | **bool** |  | [readonly] 
**changed_revision** | **int** |  | [readonly] 
**pending** | **bool** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.gateway_route import GatewayRoute

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayRoute from a JSON string
gateway_route_instance = GatewayRoute.from_json(json)
# print the JSON string representation of the object
print(GatewayRoute.to_json())

# convert the object into a dict
gateway_route_dict = gateway_route_instance.to_dict()
# create an instance of GatewayRoute from a dict
gateway_route_from_dict = GatewayRoute.from_dict(gateway_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


