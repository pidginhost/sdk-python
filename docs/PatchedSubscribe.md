# PatchedSubscribe


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier** | [**TierEnum**](TierEnum.md) |  | [optional] 

## Example

```python
from pidginhost_sdk.models.patched_subscribe import PatchedSubscribe

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedSubscribe from a JSON string
patched_subscribe_instance = PatchedSubscribe.from_json(json)
# print the JSON string representation of the object
print(PatchedSubscribe.to_json())

# convert the object into a dict
patched_subscribe_dict = patched_subscribe_instance.to_dict()
# create an instance of PatchedSubscribe from a dict
patched_subscribe_from_dict = PatchedSubscribe.from_dict(patched_subscribe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


