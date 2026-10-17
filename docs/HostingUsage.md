# HostingUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fetched_at** | **str** |  | 
**package** | **str** |  | 
**metrics** | [**List[HostingUsageMetric]**](HostingUsageMetric.md) |  | 
**live_available** | **bool** |  | 
**lve_available** | **bool** |  | 
**lve_period** | [**List[HostingLVEPeriod]**](HostingLVEPeriod.md) |  | 
**package_limits** | **Dict[str, int]** |  | 
**pressure_detected** | **bool** |  | 

## Example

```python
from pidginhost_sdk.models.hosting_usage import HostingUsage

# TODO update the JSON string below
json = "{}"
# create an instance of HostingUsage from a JSON string
hosting_usage_instance = HostingUsage.from_json(json)
# print the JSON string representation of the object
print(HostingUsage.to_json())

# convert the object into a dict
hosting_usage_dict = hosting_usage_instance.to_dict()
# create an instance of HostingUsage from a dict
hosting_usage_from_dict = HostingUsage.from_dict(hosting_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


