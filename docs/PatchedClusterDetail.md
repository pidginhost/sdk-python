# PatchedClusterDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**status** | [**StatusA57Enum**](StatusA57Enum.md) |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**cluster_type** | **str** |  | [optional] [readonly] 
**kube_version** | **str** |  | [optional] [readonly] 
**price_per_month** | **decimal.Decimal** |  | [optional] 
**price_per_hour** | **str** |  | [optional] [readonly] 
**features** | [**List[FeaturesEnum]**](FeaturesEnum.md) |  | [optional] 
**features_ready** | **bool** |  | [optional] [readonly] 
**kubeconfig_valid_until** | **str** |  | [optional] [readonly] 
**ipv4_address** | **str** |  | [optional] [readonly] 
**protected** | **bool** |  | [optional] 
**talos_version** | **str** |  | [optional] [readonly] 
**talos_upgrade_available** | **str** |  | [optional] [readonly] 
**talos_next_version** | **str** |  | [optional] [readonly] 

## Example

```python
from pidginhost_sdk.models.patched_cluster_detail import PatchedClusterDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedClusterDetail from a JSON string
patched_cluster_detail_instance = PatchedClusterDetail.from_json(json)
# print the JSON string representation of the object
print(PatchedClusterDetail.to_json())

# convert the object into a dict
patched_cluster_detail_dict = patched_cluster_detail_instance.to_dict()
# create an instance of PatchedClusterDetail from a dict
patched_cluster_detail_from_dict = PatchedClusterDetail.from_dict(patched_cluster_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


