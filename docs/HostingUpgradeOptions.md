# HostingUpgradeOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[HostingUpgradeOption]**](HostingUpgradeOption.md) |  | 

## Example

```python
from pidginhost_sdk.models.hosting_upgrade_options import HostingUpgradeOptions

# TODO update the JSON string below
json = "{}"
# create an instance of HostingUpgradeOptions from a JSON string
hosting_upgrade_options_instance = HostingUpgradeOptions.from_json(json)
# print the JSON string representation of the object
print(HostingUpgradeOptions.to_json())

# convert the object into a dict
hosting_upgrade_options_dict = hosting_upgrade_options_instance.to_dict()
# create an instance of HostingUpgradeOptions from a dict
hosting_upgrade_options_from_dict = HostingUpgradeOptions.from_dict(hosting_upgrade_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


