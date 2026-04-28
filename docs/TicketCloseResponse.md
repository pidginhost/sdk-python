# TicketCloseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.ticket_close_response import TicketCloseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TicketCloseResponse from a JSON string
ticket_close_response_instance = TicketCloseResponse.from_json(json)
# print the JSON string representation of the object
print(TicketCloseResponse.to_json())

# convert the object into a dict
ticket_close_response_dict = ticket_close_response_instance.to_dict()
# create an instance of TicketCloseResponse from a dict
ticket_close_response_from_dict = TicketCloseResponse.from_dict(ticket_close_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


