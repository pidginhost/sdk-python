# PaginatedGatewayNetworkList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[GatewayNetwork]**](GatewayNetwork.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_gateway_network_list import PaginatedGatewayNetworkList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGatewayNetworkList from a JSON string
paginated_gateway_network_list_instance = PaginatedGatewayNetworkList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGatewayNetworkList.to_json())

# convert the object into a dict
paginated_gateway_network_list_dict = paginated_gateway_network_list_instance.to_dict()
# create an instance of PaginatedGatewayNetworkList from a dict
paginated_gateway_network_list_from_dict = PaginatedGatewayNetworkList.from_dict(paginated_gateway_network_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


