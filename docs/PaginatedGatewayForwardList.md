# PaginatedGatewayForwardList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[GatewayForward]**](GatewayForward.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_gateway_forward_list import PaginatedGatewayForwardList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGatewayForwardList from a JSON string
paginated_gateway_forward_list_instance = PaginatedGatewayForwardList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGatewayForwardList.to_json())

# convert the object into a dict
paginated_gateway_forward_list_dict = paginated_gateway_forward_list_instance.to_dict()
# create an instance of PaginatedGatewayForwardList from a dict
paginated_gateway_forward_list_from_dict = PaginatedGatewayForwardList.from_dict(paginated_gateway_forward_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


