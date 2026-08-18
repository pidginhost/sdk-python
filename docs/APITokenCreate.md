# APITokenCreate

Label bound tokens with their account + membership status (spec §4.2).  A dark deployment (flag off) with only personal rows keeps the exact pre-feature response shape; a bound row is always labeled so it cannot be mistaken for a personal token even after an emergency disable.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**scope** | [**ScopeEnum**](ScopeEnum.md) |  | [optional] 
**key** | **str** |  | [readonly] 
**created** | **str** |  | [readonly] 
**account** | **str** |  | [readonly] 
**membership_status** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.api_token_create import APITokenCreate

# TODO update the JSON string below
json = "{}"
# create an instance of APITokenCreate from a JSON string
api_token_create_instance = APITokenCreate.from_json(json)
# print the JSON string representation of the object
print(APITokenCreate.to_json())

# convert the object into a dict
api_token_create_dict = api_token_create_instance.to_dict()
# create an instance of APITokenCreate from a dict
api_token_create_from_dict = APITokenCreate.from_dict(api_token_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


