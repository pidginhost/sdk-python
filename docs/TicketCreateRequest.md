# TicketCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** |  | 
**department** | **int** |  | 
**priority** | [**TicketCreatePriorityEnum**](TicketCreatePriorityEnum.md) |  | [optional] 
**service_id** | **int** |  | [optional] 
**message** | **str** |  | 
**attachment** | **bytes** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.ticket_create_request import TicketCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TicketCreateRequest from a JSON string
ticket_create_request_instance = TicketCreateRequest.from_json(json)
# print the JSON string representation of the object
print(TicketCreateRequest.to_json())

# convert the object into a dict
ticket_create_request_dict = ticket_create_request_instance.to_dict()
# create an instance of TicketCreateRequest from a dict
ticket_create_request_from_dict = TicketCreateRequest.from_dict(ticket_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


