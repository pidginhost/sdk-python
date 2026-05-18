# PaginatedFloatingIPv4List


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[FloatingIPv4]**](FloatingIPv4.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_floating_ipv4_list import PaginatedFloatingIPv4List

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedFloatingIPv4List from a JSON string
paginated_floating_ipv4_list_instance = PaginatedFloatingIPv4List.from_json(json)
# print the JSON string representation of the object
print(PaginatedFloatingIPv4List.to_json())

# convert the object into a dict
paginated_floating_ipv4_list_dict = paginated_floating_ipv4_list_instance.to_dict()
# create an instance of PaginatedFloatingIPv4List from a dict
paginated_floating_ipv4_list_from_dict = PaginatedFloatingIPv4List.from_dict(paginated_floating_ipv4_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


