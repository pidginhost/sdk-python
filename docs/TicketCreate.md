# TicketCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** |  | 
**department** | **int** |  | 
**priority** | [**TicketCreatePriorityEnum**](TicketCreatePriorityEnum.md) |  | [optional] 
**service_id** | **int** |  | [optional] 
**message** | **str** |  | 
**attachment** | **str** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.ticket_create import TicketCreate

# TODO update the JSON string below
json = "{}"
# create an instance of TicketCreate from a JSON string
ticket_create_instance = TicketCreate.from_json(json)
# print the JSON string representation of the object
print(TicketCreate.to_json())

# convert the object into a dict
ticket_create_dict = ticket_create_instance.to_dict()
# create an instance of TicketCreate from a dict
ticket_create_from_dict = TicketCreate.from_dict(ticket_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


