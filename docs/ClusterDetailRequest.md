# ClusterDetailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**price_per_month** | **decimal.Decimal** |  | 
**features** | [**List[FeaturesEnum]**](FeaturesEnum.md) |  | [optional] 
**protected** | **bool** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.cluster_detail_request import ClusterDetailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDetailRequest from a JSON string
cluster_detail_request_instance = ClusterDetailRequest.from_json(json)
# print the JSON string representation of the object
print(ClusterDetailRequest.to_json())

# convert the object into a dict
cluster_detail_request_dict = cluster_detail_request_instance.to_dict()
# create an instance of ClusterDetailRequest from a dict
cluster_detail_request_from_dict = ClusterDetailRequest.from_dict(cluster_detail_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


