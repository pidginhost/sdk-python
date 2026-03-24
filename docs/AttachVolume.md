# AttachVolume


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | **int** | Server ID | 

## Example

```python
from pidginhost_sdk.models.attach_volume import AttachVolume

# TODO update the JSON string below
json = "{}"
# create an instance of AttachVolume from a JSON string
attach_volume_instance = AttachVolume.from_json(json)
# print the JSON string representation of the object
print(AttachVolume.to_json())

# convert the object into a dict
attach_volume_dict = attach_volume_instance.to_dict()
# create an instance of AttachVolume from a dict
attach_volume_from_dict = AttachVolume.from_dict(attach_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


