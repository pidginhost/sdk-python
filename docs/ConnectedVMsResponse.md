# ConnectedVMsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vms** | [**List[ConnectedVM]**](ConnectedVM.md) |  | 

## Example

```python
from pidginhost_sdk.models.connected_vms_response import ConnectedVMsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedVMsResponse from a JSON string
connected_vms_response_instance = ConnectedVMsResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectedVMsResponse.to_json())

# convert the object into a dict
connected_vms_response_dict = connected_vms_response_instance.to_dict()
# create an instance of ConnectedVMsResponse from a dict
connected_vms_response_from_dict = ConnectedVMsResponse.from_dict(connected_vms_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


