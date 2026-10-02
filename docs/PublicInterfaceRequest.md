# PublicInterfaceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fw_rules_set** | **str** | ID or slug | [optional] 
**fw_policy_in** | [**FwPolicyOutEnum**](FwPolicyOutEnum.md) |  | [optional] 
**fw_policy_out** | [**FwPolicyOutEnum**](FwPolicyOutEnum.md) |  | [optional] 

## Example

```python
from pidginhost_sdk.models.public_interface_request import PublicInterfaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PublicInterfaceRequest from a JSON string
public_interface_request_instance = PublicInterfaceRequest.from_json(json)
# print the JSON string representation of the object
print(PublicInterfaceRequest.to_json())

# convert the object into a dict
public_interface_request_dict = public_interface_request_instance.to_dict()
# create an instance of PublicInterfaceRequest from a dict
public_interface_request_from_dict = PublicInterfaceRequest.from_dict(public_interface_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


