# PatchedClusterDetailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**price_per_month** | **decimal.Decimal** |  | [optional] 
**features** | [**List[FeaturesEnum]**](FeaturesEnum.md) |  | [optional] 
**protected** | **bool** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.patched_cluster_detail_request import PatchedClusterDetailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedClusterDetailRequest from a JSON string
patched_cluster_detail_request_instance = PatchedClusterDetailRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedClusterDetailRequest.to_json())

# convert the object into a dict
patched_cluster_detail_request_dict = patched_cluster_detail_request_instance.to_dict()
# create an instance of PatchedClusterDetailRequest from a dict
patched_cluster_detail_request_from_dict = PatchedClusterDetailRequest.from_dict(patched_cluster_detail_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


