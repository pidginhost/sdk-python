# SendRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_address** | **str** |  | 
**to** | **List[str]** |  | 
**cc** | **List[str]** |  | [optional] 
**bcc** | **List[str]** |  | [optional] 
**reply_to** | **str** |  | [optional] 
**subject** | **str** |  | 
**html_body** | **str** |  | [optional] 
**plain_body** | **str** |  | [optional] 
**headers** | **Dict[str, str]** |  | [optional] 
**track_opens** | **bool** |  | [optional] [default to False]
**track_clicks** | **bool** |  | [optional] [default to False]
**attachments** | [**List[AttachmentRequest]**](AttachmentRequest.md) |  | [optional] 

## Example

```python
from pidginhost_sdk.models.send_request import SendRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendRequest from a JSON string
send_request_instance = SendRequest.from_json(json)
# print the JSON string representation of the object
print(SendRequest.to_json())

# convert the object into a dict
send_request_dict = send_request_instance.to_dict()
# create an instance of SendRequest from a dict
send_request_from_dict = SendRequest.from_dict(send_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


