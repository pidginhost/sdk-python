# RouteStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **int** |  | 
**gateway** | **int** | The gateway that routes for the network, or null. | 
**servers** | [**List[ServerRoute]**](ServerRoute.md) |  | 
**operations** | [**List[GatewayOperation]**](GatewayOperation.md) | The network&#39;s route applies, newest first. | 

## Example

```python
from pidginhost_sdk.models.route_status import RouteStatus

# TODO update the JSON string below
json = "{}"
# create an instance of RouteStatus from a JSON string
route_status_instance = RouteStatus.from_json(json)
# print the JSON string representation of the object
print(RouteStatus.to_json())

# convert the object into a dict
route_status_dict = route_status_instance.to_dict()
# create an instance of RouteStatus from a dict
route_status_from_dict = RouteStatus.from_dict(route_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


