# AccountSessionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor_email** | **str** |  | 
**account_email** | **str** |  | 
**role** | **str** |  | 
**token_id** | **int** |  | 
**token_scope** | **str** |  | 
**capabilities** | **Dict[str, bool]** |  | 
**currency** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.account_session_response import AccountSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountSessionResponse from a JSON string
account_session_response_instance = AccountSessionResponse.from_json(json)
# print the JSON string representation of the object
print(AccountSessionResponse.to_json())

# convert the object into a dict
account_session_response_dict = account_session_response_instance.to_dict()
# create an instance of AccountSessionResponse from a dict
account_session_response_from_dict = AccountSessionResponse.from_dict(account_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


