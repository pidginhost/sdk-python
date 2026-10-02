# AttachVolumeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | **int** | Server ID | 

## Example

```python
from pidginhost_sdk.models.attach_volume_request import AttachVolumeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AttachVolumeRequest from a JSON string
attach_volume_request_instance = AttachVolumeRequest.from_json(json)
# print the JSON string representation of the object
print(AttachVolumeRequest.to_json())

# convert the object into a dict
attach_volume_request_dict = attach_volume_request_instance.to_dict()
# create an instance of AttachVolumeRequest from a dict
attach_volume_request_from_dict = AttachVolumeRequest.from_dict(attach_volume_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


