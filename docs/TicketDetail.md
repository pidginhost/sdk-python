# TicketDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**subject** | **str** |  | [readonly] 
**department** | [**Department**](Department.md) |  | [readonly] 
**priority** | [**Priority3cdEnum**](Priority3cdEnum.md) |  | [readonly] 
**status** | [**StatusEf2Enum**](StatusEf2Enum.md) |  | [readonly] 
**created** | **str** |  | [readonly] 
**updated** | **str** |  | [readonly] 
**messages** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.ticket_detail import TicketDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TicketDetail from a JSON string
ticket_detail_instance = TicketDetail.from_json(json)
# print the JSON string representation of the object
print(TicketDetail.to_json())

# convert the object into a dict
ticket_detail_dict = ticket_detail_instance.to_dict()
# create an instance of TicketDetail from a dict
ticket_detail_from_dict = TicketDetail.from_dict(ticket_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


