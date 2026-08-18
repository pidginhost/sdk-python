# PaginatedUDPRouteList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[UDPRoute]**](UDPRoute.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_udp_route_list import PaginatedUDPRouteList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUDPRouteList from a JSON string
paginated_udp_route_list_instance = PaginatedUDPRouteList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUDPRouteList.to_json())

# convert the object into a dict
paginated_udp_route_list_dict = paginated_udp_route_list_instance.to_dict()
# create an instance of PaginatedUDPRouteList from a dict
paginated_udp_route_list_from_dict = PaginatedUDPRouteList.from_dict(paginated_udp_route_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


