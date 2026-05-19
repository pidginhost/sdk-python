# PaginatedServerList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Server]**](Server.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_server_list import PaginatedServerList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedServerList from a JSON string
paginated_server_list_instance = PaginatedServerList.from_json(json)
# print the JSON string representation of the object
print(PaginatedServerList.to_json())

# convert the object into a dict
paginated_server_list_dict = paginated_server_list_instance.to_dict()
# create an instance of PaginatedServerList from a dict
paginated_server_list_from_dict = PaginatedServerList.from_dict(paginated_server_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


