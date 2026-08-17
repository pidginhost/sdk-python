# APITokenList

Label bound tokens with their account + membership status (spec §4.2).  A dark deployment (flag off) with only personal rows keeps the exact pre-feature response shape; a bound row is always labeled so it cannot be mistaken for a personal token even after an emergency disable.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | [readonly] 
**scope** | [**ScopeEnum**](ScopeEnum.md) |  | [readonly] 
**key_prefix** | **str** |  | [readonly] 
**created** | **str** |  | [readonly] 
**last_used** | **str** |  | [readonly] 
**request_count** | **int** |  | [readonly] 
**account** | **str** |  | [readonly] 
**membership_status** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.api_token_list import APITokenList

# TODO update the JSON string below
json = "{}"
# create an instance of APITokenList from a JSON string
api_token_list_instance = APITokenList.from_json(json)
# print the JSON string representation of the object
print(APITokenList.to_json())

# convert the object into a dict
api_token_list_dict = api_token_list_instance.to_dict()
# create an instance of APITokenList from a dict
api_token_list_from_dict = APITokenList.from_dict(api_token_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


