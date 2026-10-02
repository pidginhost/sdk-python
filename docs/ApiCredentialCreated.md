# ApiCredentialCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential** | [**ApiCredential**](ApiCredential.md) |  | 
**key** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.api_credential_created import ApiCredentialCreated

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCredentialCreated from a JSON string
api_credential_created_instance = ApiCredentialCreated.from_json(json)
# print the JSON string representation of the object
print(ApiCredentialCreated.to_json())

# convert the object into a dict
api_credential_created_dict = api_credential_created_instance.to_dict()
# create an instance of ApiCredentialCreated from a dict
api_credential_created_from_dict = ApiCredentialCreated.from_dict(api_credential_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


