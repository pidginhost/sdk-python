# PaginatedAPITokenListList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[APITokenList]**](APITokenList.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_api_token_list_list import PaginatedAPITokenListList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAPITokenListList from a JSON string
paginated_api_token_list_list_instance = PaginatedAPITokenListList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAPITokenListList.to_json())

# convert the object into a dict
paginated_api_token_list_list_dict = paginated_api_token_list_list_instance.to_dict()
# create an instance of PaginatedAPITokenListList from a dict
paginated_api_token_list_list_from_dict = PaginatedAPITokenListList.from_dict(paginated_api_token_list_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


