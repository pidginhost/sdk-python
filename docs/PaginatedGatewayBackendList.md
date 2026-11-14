# PaginatedGatewayBackendList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[GatewayBackend]**](GatewayBackend.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_gateway_backend_list import PaginatedGatewayBackendList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGatewayBackendList from a JSON string
paginated_gateway_backend_list_instance = PaginatedGatewayBackendList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGatewayBackendList.to_json())

# convert the object into a dict
paginated_gateway_backend_list_dict = paginated_gateway_backend_list_instance.to_dict()
# create an instance of PaginatedGatewayBackendList from a dict
paginated_gateway_backend_list_from_dict = PaginatedGatewayBackendList.from_dict(paginated_gateway_backend_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


