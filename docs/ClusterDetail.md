# ClusterDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**status** | [**StatusA57Enum**](StatusA57Enum.md) |  | [readonly] 
**name** | **str** |  | [optional] 
**cluster_type** | **str** |  | [readonly] 
**kube_version** | **str** |  | [readonly] 
**price_per_month** | **decimal.Decimal** |  | 
**price_per_hour** | **str** |  | [readonly] 
**features** | [**List[FeaturesEnum]**](FeaturesEnum.md) |  | [optional] 
**features_ready** | **bool** |  | [readonly] 
**kubeconfig_valid_until** | **str** |  | [readonly] 
**ipv4_address** | **str** |  | [readonly] 
**protected** | **bool** |  | [optional] 
**talos_version** | **str** |  | [readonly] 
**talos_upgrade_available** | **str** |  | [readonly] 
**talos_next_version** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.cluster_detail import ClusterDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDetail from a JSON string
cluster_detail_instance = ClusterDetail.from_json(json)
# print the JSON string representation of the object
print(ClusterDetail.to_json())

# convert the object into a dict
cluster_detail_dict = cluster_detail_instance.to_dict()
# create an instance of ClusterDetail from a dict
cluster_detail_from_dict = ClusterDetail.from_dict(cluster_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


