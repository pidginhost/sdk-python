# DetachVolume


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detached** | **bool** |  | 

## Example

```python
from pidginhost_sdk.models.detach_volume import DetachVolume

# TODO update the JSON string below
json = "{}"
# create an instance of DetachVolume from a JSON string
detach_volume_instance = DetachVolume.from_json(json)
# print the JSON string representation of the object
print(DetachVolume.to_json())

# convert the object into a dict
detach_volume_dict = detach_volume_instance.to_dict()
# create an instance of DetachVolume from a dict
detach_volume_from_dict = DetachVolume.from_dict(detach_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


