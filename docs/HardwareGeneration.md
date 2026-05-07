# HardwareGeneration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**cpu_label** | **str** |  | [optional] 
**price_multiplier** | **decimal.Decimal** | Multiplier applied to base MeteredProduct price (1.00 &#x3D; no change, 1.50 &#x3D; +50%) | [optional] 
**is_default** | **bool** |  | [optional] 
**icon_class** | **str** |  | [optional] 
**free_tier_eligible** | **bool** | Whether free tier VM plans are available on this generation | [optional] 

## Example

```python
from pidginhost_sdk.models.hardware_generation import HardwareGeneration

# TODO update the JSON string below
json = "{}"
# create an instance of HardwareGeneration from a JSON string
hardware_generation_instance = HardwareGeneration.from_json(json)
# print the JSON string representation of the object
print(HardwareGeneration.to_json())

# convert the object into a dict
hardware_generation_dict = hardware_generation_instance.to_dict()
# create an instance of HardwareGeneration from a dict
hardware_generation_from_dict = HardwareGeneration.from_dict(hardware_generation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


