# PaginatedPrivateNetworkList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PrivateNetwork]**](PrivateNetwork.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_private_network_list import PaginatedPrivateNetworkList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPrivateNetworkList from a JSON string
paginated_private_network_list_instance = PaginatedPrivateNetworkList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPrivateNetworkList.to_json())

# convert the object into a dict
paginated_private_network_list_dict = paginated_private_network_list_instance.to_dict()
# create an instance of PaginatedPrivateNetworkList from a dict
paginated_private_network_list_from_dict = PaginatedPrivateNetworkList.from_dict(paginated_private_network_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


