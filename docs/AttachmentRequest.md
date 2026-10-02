# AttachmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**content_type** | **str** |  | 
**data** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.attachment_request import AttachmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentRequest from a JSON string
attachment_request_instance = AttachmentRequest.from_json(json)
# print the JSON string representation of the object
print(AttachmentRequest.to_json())

# convert the object into a dict
attachment_request_dict = attachment_request_instance.to_dict()
# create an instance of AttachmentRequest from a dict
attachment_request_from_dict = AttachmentRequest.from_dict(attachment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


