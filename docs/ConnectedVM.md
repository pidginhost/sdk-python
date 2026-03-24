# ConnectedVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**hostname** | **str** |  | 
**ip** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.connected_vm import ConnectedVM

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedVM from a JSON string
connected_vm_instance = ConnectedVM.from_json(json)
# print the JSON string representation of the object
print(ConnectedVM.to_json())

# convert the object into a dict
connected_vm_dict = connected_vm_instance.to_dict()
# create an instance of ConnectedVM from a dict
connected_vm_from_dict = ConnectedVM.from_dict(connected_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


