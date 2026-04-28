# ClusterPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**slug** | **str** |  | 
**name** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.cluster_package import ClusterPackage

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterPackage from a JSON string
cluster_package_instance = ClusterPackage.from_json(json)
# print the JSON string representation of the object
print(ClusterPackage.to_json())

# convert the object into a dict
cluster_package_dict = cluster_package_instance.to_dict()
# create an instance of ClusterPackage from a dict
cluster_package_from_dict = ClusterPackage.from_dict(cluster_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


