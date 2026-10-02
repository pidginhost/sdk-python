# TicketReplyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**attachment** | **bytes** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.ticket_reply_request import TicketReplyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TicketReplyRequest from a JSON string
ticket_reply_request_instance = TicketReplyRequest.from_json(json)
# print the JSON string representation of the object
print(TicketReplyRequest.to_json())

# convert the object into a dict
ticket_reply_request_dict = ticket_reply_request_instance.to_dict()
# create an instance of TicketReplyRequest from a dict
ticket_reply_request_from_dict = TicketReplyRequest.from_dict(ticket_reply_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


