# PaginatedDomainRegistrantList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[DomainRegistrant]**](DomainRegistrant.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_domain_registrant_list import PaginatedDomainRegistrantList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedDomainRegistrantList from a JSON string
paginated_domain_registrant_list_instance = PaginatedDomainRegistrantList.from_json(json)
# print the JSON string representation of the object
print(PaginatedDomainRegistrantList.to_json())

# convert the object into a dict
paginated_domain_registrant_list_dict = paginated_domain_registrant_list_instance.to_dict()
# create an instance of PaginatedDomainRegistrantList from a dict
paginated_domain_registrant_list_from_dict = PaginatedDomainRegistrantList.from_dict(paginated_domain_registrant_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


