# OSImage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**slug** | **str** |  | 
**name** | **str** | Display name for users | 
**family_name** | **str** |  | [readonly] 
**is_default** | **bool** | Default version within this family (shown pre-selected) | [optional] 

## Example

```python
from pidginhost_sdk.models.os_image import OSImage

# TODO update the JSON string below
json = "{}"
# create an instance of OSImage from a JSON string
os_image_instance = OSImage.from_json(json)
# print the JSON string representation of the object
print(OSImage.to_json())

# convert the object into a dict
os_image_dict = os_image_instance.to_dict()
# create an instance of OSImage from a dict
os_image_from_dict = OSImage.from_dict(os_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


