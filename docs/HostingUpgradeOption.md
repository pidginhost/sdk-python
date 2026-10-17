# HostingUpgradeOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**base_price** | **float** |  | 
**currency** | **str** |  | 
**tax_included** | **bool** |  | 
**limits** | **Dict[str, object]** | Package display limits; disk_quota and traffic are in GB. | 
**review_url** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.hosting_upgrade_option import HostingUpgradeOption

# TODO update the JSON string below
json = "{}"
# create an instance of HostingUpgradeOption from a JSON string
hosting_upgrade_option_instance = HostingUpgradeOption.from_json(json)
# print the JSON string representation of the object
print(HostingUpgradeOption.to_json())

# convert the object into a dict
hosting_upgrade_option_dict = hosting_upgrade_option_instance.to_dict()
# create an instance of HostingUpgradeOption from a dict
hosting_upgrade_option_from_dict = HostingUpgradeOption.from_dict(hosting_upgrade_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


