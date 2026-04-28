# ClusterAdd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_type** | [**ClusterTypeEnum**](ClusterTypeEnum.md) |  | 
**name** | **str** |  | [optional] 
**resource_pool_package** | **str** | ID or slug | 
**resource_pool_size** | **int** |  | [optional] 
**kube_version** | [**KubeVersionEnum**](KubeVersionEnum.md) |  | [optional] 
**features** | [**List[FeaturesEnum]**](FeaturesEnum.md) |  | [optional] 
**enable_gateway_api** | **bool** |  | [optional] 
**generation** | **str** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.cluster_add import ClusterAdd

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAdd from a JSON string
cluster_add_instance = ClusterAdd.from_json(json)
# print the JSON string representation of the object
print(ClusterAdd.to_json())

# convert the object into a dict
cluster_add_dict = cluster_add_instance.to_dict()
# create an instance of ClusterAdd from a dict
cluster_add_from_dict = ClusterAdd.from_dict(cluster_add_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


