# DisconnectVMRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server** | **int** | VM resource PK | 

## Example

```python
from pidginhost_sdk.models.disconnect_vm_request import DisconnectVMRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DisconnectVMRequest from a JSON string
disconnect_vm_request_instance = DisconnectVMRequest.from_json(json)
# print the JSON string representation of the object
print(DisconnectVMRequest.to_json())

# convert the object into a dict
disconnect_vm_request_dict = disconnect_vm_request_instance.to_dict()
# create an instance of DisconnectVMRequest from a dict
disconnect_vm_request_from_dict = DisconnectVMRequest.from_dict(disconnect_vm_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


