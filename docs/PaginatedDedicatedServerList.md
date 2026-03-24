# PaginatedDedicatedServerList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[DedicatedServer]**](DedicatedServer.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_dedicated_server_list import PaginatedDedicatedServerList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedDedicatedServerList from a JSON string
paginated_dedicated_server_list_instance = PaginatedDedicatedServerList.from_json(json)
# print the JSON string representation of the object
print(PaginatedDedicatedServerList.to_json())

# convert the object into a dict
paginated_dedicated_server_list_dict = paginated_dedicated_server_list_instance.to_dict()
# create an instance of PaginatedDedicatedServerList from a dict
paginated_dedicated_server_list_from_dict = PaginatedDedicatedServerList.from_dict(paginated_dedicated_server_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


