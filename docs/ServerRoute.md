# ServerRoute

A server's default route on the network (spec 6.3): cloud-init evidence from Proxmox, not proof that the running guest has the route. A server Proxmox could not tell about is unknown.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server** | **int** |  | 
**hostname** | **str** |  | 
**power** | [**RoutePowerEnum**](RoutePowerEnum.md) |  | 
**config** | [**RouteConfigEnum**](RouteConfigEnum.md) | The spec 6.2 rule over current config.  * &#x60;ok&#x60; - ok * &#x60;missing&#x60; - missing * &#x60;duplicate&#x60; - duplicate * &#x60;obsolete&#x60; - obsolete * &#x60;unknown&#x60; - unknown | 
**pending** | [**RouteConfigEnum**](RouteConfigEnum.md) | The rule over the config a reboot applies; null without one.  * &#x60;ok&#x60; - ok * &#x60;missing&#x60; - missing * &#x60;duplicate&#x60; - duplicate * &#x60;obsolete&#x60; - obsolete * &#x60;unknown&#x60; - unknown | 
**routes_here** | **bool** | The rule gives this network&#39;s interface the default route. | 
**acknowledged** | **bool** | The last route apply&#39;s config and boot still hold. | 

## Example

```python
from pidginhost_sdk.models.server_route import ServerRoute

# TODO update the JSON string below
json = "{}"
# create an instance of ServerRoute from a JSON string
server_route_instance = ServerRoute.from_json(json)
# print the JSON string representation of the object
print(ServerRoute.to_json())

# convert the object into a dict
server_route_dict = server_route_instance.to_dict()
# create an instance of ServerRoute from a dict
server_route_from_dict = ServerRoute.from_dict(server_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


