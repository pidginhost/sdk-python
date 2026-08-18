# PaginatedApiCredentialList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ApiCredential]**](ApiCredential.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_api_credential_list import PaginatedApiCredentialList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedApiCredentialList from a JSON string
paginated_api_credential_list_instance = PaginatedApiCredentialList.from_json(json)
# print the JSON string representation of the object
print(PaginatedApiCredentialList.to_json())

# convert the object into a dict
paginated_api_credential_list_dict = paginated_api_credential_list_instance.to_dict()
# create an instance of PaginatedApiCredentialList from a dict
paginated_api_credential_list_from_dict = PaginatedApiCredentialList.from_dict(paginated_api_credential_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


