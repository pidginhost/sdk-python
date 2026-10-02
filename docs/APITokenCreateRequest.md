# APITokenCreateRequest

Label bound tokens with their account + membership status (spec §4.2).  A dark deployment (flag off) with only personal rows keeps the exact pre-feature response shape; a bound row is always labeled so it cannot be mistaken for a personal token even after an emergency disable.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**scope** | [**ScopeEnum**](ScopeEnum.md) |  | [optional] 

## Example

```python
from pidginhost_sdk.models.api_token_create_request import APITokenCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of APITokenCreateRequest from a JSON string
api_token_create_request_instance = APITokenCreateRequest.from_json(json)
# print the JSON string representation of the object
print(APITokenCreateRequest.to_json())

# convert the object into a dict
api_token_create_request_dict = api_token_create_request_instance.to_dict()
# create an instance of APITokenCreateRequest from a dict
api_token_create_request_from_dict = APITokenCreateRequest.from_dict(api_token_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


