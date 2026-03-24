# PaginatedHostingServiceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[HostingService]**](HostingService.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_hosting_service_list import PaginatedHostingServiceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedHostingServiceList from a JSON string
paginated_hosting_service_list_instance = PaginatedHostingServiceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedHostingServiceList.to_json())

# convert the object into a dict
paginated_hosting_service_list_dict = paginated_hosting_service_list_instance.to_dict()
# create an instance of PaginatedHostingServiceList from a dict
paginated_hosting_service_list_from_dict = PaginatedHostingServiceList.from_dict(paginated_hosting_service_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


