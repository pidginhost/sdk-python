# PaginatedResourcePoolList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ResourcePool]**](ResourcePool.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_resource_pool_list import PaginatedResourcePoolList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResourcePoolList from a JSON string
paginated_resource_pool_list_instance = PaginatedResourcePoolList.from_json(json)
# print the JSON string representation of the object
print(PaginatedResourcePoolList.to_json())

# convert the object into a dict
paginated_resource_pool_list_dict = paginated_resource_pool_list_instance.to_dict()
# create an instance of PaginatedResourcePoolList from a dict
paginated_resource_pool_list_from_dict = PaginatedResourcePoolList.from_dict(paginated_resource_pool_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


