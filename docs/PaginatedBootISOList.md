# PaginatedBootISOList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[BootISO]**](BootISO.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_boot_iso_list import PaginatedBootISOList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedBootISOList from a JSON string
paginated_boot_iso_list_instance = PaginatedBootISOList.from_json(json)
# print the JSON string representation of the object
print(PaginatedBootISOList.to_json())

# convert the object into a dict
paginated_boot_iso_list_dict = paginated_boot_iso_list_instance.to_dict()
# create an instance of PaginatedBootISOList from a dict
paginated_boot_iso_list_from_dict = PaginatedBootISOList.from_dict(paginated_boot_iso_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


