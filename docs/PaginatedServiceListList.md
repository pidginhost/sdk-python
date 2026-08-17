# PaginatedServiceListList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ServiceList]**](ServiceList.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_service_list_list import PaginatedServiceListList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedServiceListList from a JSON string
paginated_service_list_list_instance = PaginatedServiceListList.from_json(json)
# print the JSON string representation of the object
print(PaginatedServiceListList.to_json())

# convert the object into a dict
paginated_service_list_list_dict = paginated_service_list_list_instance.to_dict()
# create an instance of PaginatedServiceListList from a dict
paginated_service_list_list_from_dict = PaginatedServiceListList.from_dict(paginated_service_list_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


