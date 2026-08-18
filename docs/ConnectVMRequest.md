# ConnectVMRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server** | **int** | VM resource PK or hostname | 

## Example

```python
from pidginhost_sdk.models.connect_vm_request import ConnectVMRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectVMRequest from a JSON string
connect_vm_request_instance = ConnectVMRequest.from_json(json)
# print the JSON string representation of the object
print(ConnectVMRequest.to_json())

# convert the object into a dict
connect_vm_request_dict = connect_vm_request_instance.to_dict()
# create an instance of ConnectVMRequest from a dict
connect_vm_request_from_dict = ConnectVMRequest.from_dict(connect_vm_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


