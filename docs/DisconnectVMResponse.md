# DisconnectVMResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.disconnect_vm_response import DisconnectVMResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DisconnectVMResponse from a JSON string
disconnect_vm_response_instance = DisconnectVMResponse.from_json(json)
# print the JSON string representation of the object
print(DisconnectVMResponse.to_json())

# convert the object into a dict
disconnect_vm_response_dict = disconnect_vm_response_instance.to_dict()
# create an instance of DisconnectVMResponse from a dict
disconnect_vm_response_from_dict = DisconnectVMResponse.from_dict(disconnect_vm_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


