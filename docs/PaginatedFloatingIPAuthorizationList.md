# PaginatedFloatingIPAuthorizationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[FloatingIPAuthorization]**](FloatingIPAuthorization.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_floating_ip_authorization_list import PaginatedFloatingIPAuthorizationList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedFloatingIPAuthorizationList from a JSON string
paginated_floating_ip_authorization_list_instance = PaginatedFloatingIPAuthorizationList.from_json(json)
# print the JSON string representation of the object
print(PaginatedFloatingIPAuthorizationList.to_json())

# convert the object into a dict
paginated_floating_ip_authorization_list_dict = paginated_floating_ip_authorization_list_instance.to_dict()
# create an instance of PaginatedFloatingIPAuthorizationList from a dict
paginated_floating_ip_authorization_list_from_dict = PaginatedFloatingIPAuthorizationList.from_dict(paginated_floating_ip_authorization_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


