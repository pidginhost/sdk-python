# MobileOAuthSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor_email** | **str** |  | 
**account_email** | **str** |  | 
**role** | **str** |  | 
**token_id** | **int** |  | 
**token_scope** | **str** |  | 
**currency** | **str** |  | 
**capabilities** | **Dict[str, bool]** |  | 

## Example

```python
from pidginhost_sdk.models.mobile_o_auth_session import MobileOAuthSession

# TODO update the JSON string below
json = "{}"
# create an instance of MobileOAuthSession from a JSON string
mobile_o_auth_session_instance = MobileOAuthSession.from_json(json)
# print the JSON string representation of the object
print(MobileOAuthSession.to_json())

# convert the object into a dict
mobile_o_auth_session_dict = mobile_o_auth_session_instance.to_dict()
# create an instance of MobileOAuthSession from a dict
mobile_o_auth_session_from_dict = MobileOAuthSession.from_dict(mobile_o_auth_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


