# PaginatedSendingDomainList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[SendingDomain]**](SendingDomain.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_sending_domain_list import PaginatedSendingDomainList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSendingDomainList from a JSON string
paginated_sending_domain_list_instance = PaginatedSendingDomainList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSendingDomainList.to_json())

# convert the object into a dict
paginated_sending_domain_list_dict = paginated_sending_domain_list_instance.to_dict()
# create an instance of PaginatedSendingDomainList from a dict
paginated_sending_domain_list_from_dict = PaginatedSendingDomainList.from_dict(paginated_sending_domain_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


