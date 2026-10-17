# DedicatedHardware


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**processor** | **str** |  | 
**processor_count** | **int** |  | 
**memory_gb** | **int** |  | 
**disks** | **str** |  | 
**raid** | **str** |  | 
**network** | **str** |  | 
**traffic** | **str** |  | 
**gpu** | **str** |  | 
**extra_hardware** | **List[str]** |  | 
**software** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.dedicated_hardware import DedicatedHardware

# TODO update the JSON string below
json = "{}"
# create an instance of DedicatedHardware from a JSON string
dedicated_hardware_instance = DedicatedHardware.from_json(json)
# print the JSON string representation of the object
print(DedicatedHardware.to_json())

# convert the object into a dict
dedicated_hardware_dict = dedicated_hardware_instance.to_dict()
# create an instance of DedicatedHardware from a dict
dedicated_hardware_from_dict = DedicatedHardware.from_dict(dedicated_hardware_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


