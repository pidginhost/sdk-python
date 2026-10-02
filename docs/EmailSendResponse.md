# EmailSendResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **object** |  | 
**queued_at** | **str** |  | 
**status** | [**EmailSendResponseStatusEnum**](EmailSendResponseStatusEnum.md) |  | 

## Example

```python
from pidginhost_sdk.models.email_send_response import EmailSendResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmailSendResponse from a JSON string
email_send_response_instance = EmailSendResponse.from_json(json)
# print the JSON string representation of the object
print(EmailSendResponse.to_json())

# convert the object into a dict
email_send_response_dict = email_send_response_instance.to_dict()
# create an instance of EmailSendResponse from a dict
email_send_response_from_dict = EmailSendResponse.from_dict(email_send_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


