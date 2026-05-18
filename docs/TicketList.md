# TicketList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**subject** | **str** |  | [readonly] 
**department** | **str** |  | [readonly] 
**priority** | [**Priority3cdEnum**](Priority3cdEnum.md) |  | [readonly] 
**status** | [**StatusEf2Enum**](StatusEf2Enum.md) |  | [readonly] 
**created** | **str** |  | [readonly] 
**updated** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.ticket_list import TicketList

# TODO update the JSON string below
json = "{}"
# create an instance of TicketList from a JSON string
ticket_list_instance = TicketList.from_json(json)
# print the JSON string representation of the object
print(TicketList.to_json())

# convert the object into a dict
ticket_list_dict = ticket_list_instance.to_dict()
# create an instance of TicketList from a dict
ticket_list_from_dict = TicketList.from_dict(ticket_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


