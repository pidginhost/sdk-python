# VolumeBusy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [readonly] 
**extra** | **Dict[str, object]** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.volume_busy import VolumeBusy

# TODO update the JSON string below
json = "{}"
# create an instance of VolumeBusy from a JSON string
volume_busy_instance = VolumeBusy.from_json(json)
# print the JSON string representation of the object
print(VolumeBusy.to_json())

# convert the object into a dict
volume_busy_dict = volume_busy_instance.to_dict()
# create an instance of VolumeBusy from a dict
volume_busy_from_dict = VolumeBusy.from_dict(volume_busy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


