# PaginatedSandboxAddressList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[SandboxAddress]**](SandboxAddress.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_sandbox_address_list import PaginatedSandboxAddressList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSandboxAddressList from a JSON string
paginated_sandbox_address_list_instance = PaginatedSandboxAddressList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSandboxAddressList.to_json())

# convert the object into a dict
paginated_sandbox_address_list_dict = paginated_sandbox_address_list_instance.to_dict()
# create an instance of PaginatedSandboxAddressList from a dict
paginated_sandbox_address_list_from_dict = PaginatedSandboxAddressList.from_dict(paginated_sandbox_address_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


