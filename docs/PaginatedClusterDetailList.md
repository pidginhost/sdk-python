# PaginatedClusterDetailList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ClusterDetail]**](ClusterDetail.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_cluster_detail_list import PaginatedClusterDetailList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedClusterDetailList from a JSON string
paginated_cluster_detail_list_instance = PaginatedClusterDetailList.from_json(json)
# print the JSON string representation of the object
print(PaginatedClusterDetailList.to_json())

# convert the object into a dict
paginated_cluster_detail_list_dict = paginated_cluster_detail_list_instance.to_dict()
# create an instance of PaginatedClusterDetailList from a dict
paginated_cluster_detail_list_from_dict = PaginatedClusterDetailList.from_dict(paginated_cluster_detail_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


