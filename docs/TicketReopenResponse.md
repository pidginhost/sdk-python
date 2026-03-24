# TicketReopenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.ticket_reopen_response import TicketReopenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TicketReopenResponse from a JSON string
ticket_reopen_response_instance = TicketReopenResponse.from_json(json)
# print the JSON string representation of the object
print(TicketReopenResponse.to_json())

# convert the object into a dict
ticket_reopen_response_dict = ticket_reopen_response_instance.to_dict()
# create an instance of TicketReopenResponse from a dict
ticket_reopen_response_from_dict = TicketReopenResponse.from_dict(ticket_reopen_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


