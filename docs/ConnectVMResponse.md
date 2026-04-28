# ConnectVMResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.connect_vm_response import ConnectVMResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectVMResponse from a JSON string
connect_vm_response_instance = ConnectVMResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectVMResponse.to_json())

# convert the object into a dict
connect_vm_response_dict = connect_vm_response_instance.to_dict()
# create an instance of ConnectVMResponse from a dict
connect_vm_response_from_dict = ConnectVMResponse.from_dict(connect_vm_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


