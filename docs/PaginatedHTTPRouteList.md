# PaginatedHTTPRouteList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[HTTPRoute]**](HTTPRoute.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_http_route_list import PaginatedHTTPRouteList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedHTTPRouteList from a JSON string
paginated_http_route_list_instance = PaginatedHTTPRouteList.from_json(json)
# print the JSON string representation of the object
print(PaginatedHTTPRouteList.to_json())

# convert the object into a dict
paginated_http_route_list_dict = paginated_http_route_list_instance.to_dict()
# create an instance of PaginatedHTTPRouteList from a dict
paginated_http_route_list_from_dict = PaginatedHTTPRouteList.from_dict(paginated_http_route_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


