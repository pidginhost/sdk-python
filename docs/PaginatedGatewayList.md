# PaginatedGatewayList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Gateway]**](Gateway.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_gateway_list import PaginatedGatewayList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGatewayList from a JSON string
paginated_gateway_list_instance = PaginatedGatewayList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGatewayList.to_json())

# convert the object into a dict
paginated_gateway_list_dict = paginated_gateway_list_instance.to_dict()
# create an instance of PaginatedGatewayList from a dict
paginated_gateway_list_from_dict = PaginatedGatewayList.from_dict(paginated_gateway_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


