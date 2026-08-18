# PaginatedFloatingIPv6List


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[FloatingIPv6]**](FloatingIPv6.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_floating_ipv6_list import PaginatedFloatingIPv6List

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedFloatingIPv6List from a JSON string
paginated_floating_ipv6_list_instance = PaginatedFloatingIPv6List.from_json(json)
# print the JSON string representation of the object
print(PaginatedFloatingIPv6List.to_json())

# convert the object into a dict
paginated_floating_ipv6_list_dict = paginated_floating_ipv6_list_instance.to_dict()
# create an instance of PaginatedFloatingIPv6List from a dict
paginated_floating_ipv6_list_from_dict = PaginatedFloatingIPv6List.from_dict(paginated_floating_ipv6_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


