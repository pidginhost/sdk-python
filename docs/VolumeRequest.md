# VolumeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project** | **str** |  | [optional] 
**alias** | **str** |  | [optional] 
**size** | **int** | GB | 
**product** | **str** | ID or slug | 

## Example

```python
from pidginhost_sdk.models.volume_request import VolumeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VolumeRequest from a JSON string
volume_request_instance = VolumeRequest.from_json(json)
# print the JSON string representation of the object
print(VolumeRequest.to_json())

# convert the object into a dict
volume_request_dict = volume_request_instance.to_dict()
# create an instance of VolumeRequest from a dict
volume_request_from_dict = VolumeRequest.from_dict(volume_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


