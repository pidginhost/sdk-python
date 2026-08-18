# BootISO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**category** | [**CategoryEnum**](CategoryEnum.md) |  | [optional] 
**min_disk_size** | **int** | GB, 0 &#x3D; no minimum | [optional] 
**min_ram** | **decimal.Decimal** | GB, 0 &#x3D; no minimum | [optional] 
**wipes_disk** | **bool** | Installer media — show the data-loss warning | [optional] 
**compatible** | **bool** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.boot_iso import BootISO

# TODO update the JSON string below
json = "{}"
# create an instance of BootISO from a JSON string
boot_iso_instance = BootISO.from_json(json)
# print the JSON string representation of the object
print(BootISO.to_json())

# convert the object into a dict
boot_iso_dict = boot_iso_instance.to_dict()
# create an instance of BootISO from a dict
boot_iso_from_dict = BootISO.from_dict(boot_iso_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


