# FloatingIPSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**version** | [**VersionEnum**](VersionEnum.md) |  | [readonly] 
**address** | **str** |  | [readonly] 
**label** | **str** |  | [readonly] 
**reverse_dns** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.floating_ip_summary import FloatingIPSummary

# TODO update the JSON string below
json = "{}"
# create an instance of FloatingIPSummary from a JSON string
floating_ip_summary_instance = FloatingIPSummary.from_json(json)
# print the JSON string representation of the object
print(FloatingIPSummary.to_json())

# convert the object into a dict
floating_ip_summary_dict = floating_ip_summary_instance.to_dict()
# create an instance of FloatingIPSummary from a dict
floating_ip_summary_from_dict = FloatingIPSummary.from_dict(floating_ip_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


