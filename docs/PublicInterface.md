# PublicInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **str** |  | [readonly] 
**ipv4** | **str** |  | [readonly] 
**ipv6** | **str** |  | [readonly] 
**fw_rules_set** | **str** | ID or slug | [optional] 
**fw_policy_in** | [**FwPolicyOutEnum**](FwPolicyOutEnum.md) |  | [optional] 
**fw_policy_out** | [**FwPolicyOutEnum**](FwPolicyOutEnum.md) |  | [optional] 

## Example

```python
from pidginhost_sdk.models.public_interface import PublicInterface

# TODO update the JSON string below
json = "{}"
# create an instance of PublicInterface from a JSON string
public_interface_instance = PublicInterface.from_json(json)
# print the JSON string representation of the object
print(PublicInterface.to_json())

# convert the object into a dict
public_interface_dict = public_interface_instance.to_dict()
# create an instance of PublicInterface from a dict
public_interface_from_dict = PublicInterface.from_dict(public_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


