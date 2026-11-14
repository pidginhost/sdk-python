# PaginatedGatewayLBListenerList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[GatewayLBListener]**](GatewayLBListener.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_gateway_lb_listener_list import PaginatedGatewayLBListenerList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGatewayLBListenerList from a JSON string
paginated_gateway_lb_listener_list_instance = PaginatedGatewayLBListenerList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGatewayLBListenerList.to_json())

# convert the object into a dict
paginated_gateway_lb_listener_list_dict = paginated_gateway_lb_listener_list_instance.to_dict()
# create an instance of PaginatedGatewayLBListenerList from a dict
paginated_gateway_lb_listener_list_from_dict = PaginatedGatewayLBListenerList.from_dict(paginated_gateway_lb_listener_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


