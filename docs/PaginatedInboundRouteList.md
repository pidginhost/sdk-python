# PaginatedInboundRouteList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[InboundRoute]**](InboundRoute.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_inbound_route_list import PaginatedInboundRouteList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedInboundRouteList from a JSON string
paginated_inbound_route_list_instance = PaginatedInboundRouteList.from_json(json)
# print the JSON string representation of the object
print(PaginatedInboundRouteList.to_json())

# convert the object into a dict
paginated_inbound_route_list_dict = paginated_inbound_route_list_instance.to_dict()
# create an instance of PaginatedInboundRouteList from a dict
paginated_inbound_route_list_from_dict = PaginatedInboundRouteList.from_dict(paginated_inbound_route_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


