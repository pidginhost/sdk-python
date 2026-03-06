# TicketReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**attachment** | **str** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.ticket_reply import TicketReply

# TODO update the JSON string below
json = "{}"
# create an instance of TicketReply from a JSON string
ticket_reply_instance = TicketReply.from_json(json)
# print the JSON string representation of the object
print(TicketReply.to_json())

# convert the object into a dict
ticket_reply_dict = ticket_reply_instance.to_dict()
# create an instance of TicketReply from a dict
ticket_reply_from_dict = TicketReply.from_dict(ticket_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


