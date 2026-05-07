# PaginatedTicketListList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[TicketList]**](TicketList.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_ticket_list_list import PaginatedTicketListList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTicketListList from a JSON string
paginated_ticket_list_list_instance = PaginatedTicketListList.from_json(json)
# print the JSON string representation of the object
print(PaginatedTicketListList.to_json())

# convert the object into a dict
paginated_ticket_list_list_dict = paginated_ticket_list_list_instance.to_dict()
# create an instance of PaginatedTicketListList from a dict
paginated_ticket_list_list_from_dict = PaginatedTicketListList.from_dict(paginated_ticket_list_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


