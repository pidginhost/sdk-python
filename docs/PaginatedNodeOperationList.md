# PaginatedNodeOperationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[NodeOperation]**](NodeOperation.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_node_operation_list import PaginatedNodeOperationList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedNodeOperationList from a JSON string
paginated_node_operation_list_instance = PaginatedNodeOperationList.from_json(json)
# print the JSON string representation of the object
print(PaginatedNodeOperationList.to_json())

# convert the object into a dict
paginated_node_operation_list_dict = paginated_node_operation_list_instance.to_dict()
# create an instance of PaginatedNodeOperationList from a dict
paginated_node_operation_list_from_dict = PaginatedNodeOperationList.from_dict(paginated_node_operation_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


