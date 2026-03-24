# PaginatedResourcePoolNodeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ResourcePoolNode]**](ResourcePoolNode.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_resource_pool_node_list import PaginatedResourcePoolNodeList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResourcePoolNodeList from a JSON string
paginated_resource_pool_node_list_instance = PaginatedResourcePoolNodeList.from_json(json)
# print the JSON string representation of the object
print(PaginatedResourcePoolNodeList.to_json())

# convert the object into a dict
paginated_resource_pool_node_list_dict = paginated_resource_pool_node_list_instance.to_dict()
# create an instance of PaginatedResourcePoolNodeList from a dict
paginated_resource_pool_node_list_from_dict = PaginatedResourcePoolNodeList.from_dict(paginated_resource_pool_node_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


