# TicketReplyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.ticket_reply_response import TicketReplyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TicketReplyResponse from a JSON string
ticket_reply_response_instance = TicketReplyResponse.from_json(json)
# print the JSON string representation of the object
print(TicketReplyResponse.to_json())

# convert the object into a dict
ticket_reply_response_dict = ticket_reply_response_instance.to_dict()
# create an instance of TicketReplyResponse from a dict
ticket_reply_response_from_dict = TicketReplyResponse.from_dict(ticket_reply_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


