# PaginatedClusterTypeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ClusterType]**](ClusterType.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_cluster_type_list import PaginatedClusterTypeList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedClusterTypeList from a JSON string
paginated_cluster_type_list_instance = PaginatedClusterTypeList.from_json(json)
# print the JSON string representation of the object
print(PaginatedClusterTypeList.to_json())

# convert the object into a dict
paginated_cluster_type_list_dict = paginated_cluster_type_list_instance.to_dict()
# create an instance of PaginatedClusterTypeList from a dict
paginated_cluster_type_list_from_dict = PaginatedClusterTypeList.from_dict(paginated_cluster_type_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


