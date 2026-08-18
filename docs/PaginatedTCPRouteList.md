# PaginatedTCPRouteList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[TCPRoute]**](TCPRoute.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_tcp_route_list import PaginatedTCPRouteList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTCPRouteList from a JSON string
paginated_tcp_route_list_instance = PaginatedTCPRouteList.from_json(json)
# print the JSON string representation of the object
print(PaginatedTCPRouteList.to_json())

# convert the object into a dict
paginated_tcp_route_list_dict = paginated_tcp_route_list_instance.to_dict()
# create an instance of PaginatedTCPRouteList from a dict
paginated_tcp_route_list_from_dict = PaginatedTCPRouteList.from_dict(paginated_tcp_route_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


