# ClusterType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**Type2faEnum**](Type2faEnum.md) |  | 
**worker_nodes_count_min** | **int** |  | [optional] 
**worker_nodes_count_max** | **int** |  | [optional] 
**worker_node_packages** | [**List[ClusterPackage]**](ClusterPackage.md) |  | 

## Example

```python
from pidginhost_sdk.models.cluster_type import ClusterType

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterType from a JSON string
cluster_type_instance = ClusterType.from_json(json)
# print the JSON string representation of the object
print(ClusterType.to_json())

# convert the object into a dict
cluster_type_dict = cluster_type_instance.to_dict()
# create an instance of ClusterType from a dict
cluster_type_from_dict = ClusterType.from_dict(cluster_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


