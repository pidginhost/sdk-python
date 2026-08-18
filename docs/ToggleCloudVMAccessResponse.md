# ToggleCloudVMAccessResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**message** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.toggle_cloud_vm_access_response import ToggleCloudVMAccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ToggleCloudVMAccessResponse from a JSON string
toggle_cloud_vm_access_response_instance = ToggleCloudVMAccessResponse.from_json(json)
# print the JSON string representation of the object
print(ToggleCloudVMAccessResponse.to_json())

# convert the object into a dict
toggle_cloud_vm_access_response_dict = toggle_cloud_vm_access_response_instance.to_dict()
# create an instance of ToggleCloudVMAccessResponse from a dict
toggle_cloud_vm_access_response_from_dict = ToggleCloudVMAccessResponse.from_dict(toggle_cloud_vm_access_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


