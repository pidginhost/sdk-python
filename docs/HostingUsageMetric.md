# HostingUsageMetric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**label** | **str** |  | 
**used** | **float** |  | 
**limit** | **float** |  | 
**unit** | **str** |  | 
**percentage** | **float** |  | 
**faults** | **float** |  | [optional] 
**source** | **str** |  | 
**near_limit** | **bool** |  | 

## Example

```python
from pidginhost_sdk.models.hosting_usage_metric import HostingUsageMetric

# TODO update the JSON string below
json = "{}"
# create an instance of HostingUsageMetric from a JSON string
hosting_usage_metric_instance = HostingUsageMetric.from_json(json)
# print the JSON string representation of the object
print(HostingUsageMetric.to_json())

# convert the object into a dict
hosting_usage_metric_dict = hosting_usage_metric_instance.to_dict()
# create an instance of HostingUsageMetric from a dict
hosting_usage_metric_from_dict = HostingUsageMetric.from_dict(hosting_usage_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


