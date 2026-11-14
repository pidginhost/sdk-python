# PaginatedGatewayRouteList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[GatewayRoute]**](GatewayRoute.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_gateway_route_list import PaginatedGatewayRouteList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGatewayRouteList from a JSON string
paginated_gateway_route_list_instance = PaginatedGatewayRouteList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGatewayRouteList.to_json())

# convert the object into a dict
paginated_gateway_route_list_dict = paginated_gateway_route_list_instance.to_dict()
# create an instance of PaginatedGatewayRouteList from a dict
paginated_gateway_route_list_from_dict = PaginatedGatewayRouteList.from_dict(paginated_gateway_route_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


