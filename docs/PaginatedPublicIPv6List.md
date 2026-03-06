# PaginatedPublicIPv6List


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PublicIPv6]**](PublicIPv6.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_public_ipv6_list import PaginatedPublicIPv6List

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPublicIPv6List from a JSON string
paginated_public_ipv6_list_instance = PaginatedPublicIPv6List.from_json(json)
# print the JSON string representation of the object
print(PaginatedPublicIPv6List.to_json())

# convert the object into a dict
paginated_public_ipv6_list_dict = paginated_public_ipv6_list_instance.to_dict()
# create an instance of PaginatedPublicIPv6List from a dict
paginated_public_ipv6_list_from_dict = PaginatedPublicIPv6List.from_dict(paginated_public_ipv6_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


