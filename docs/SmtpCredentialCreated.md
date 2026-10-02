# SmtpCredentialCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential** | [**SmtpCredential**](SmtpCredential.md) |  | 
**password** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.smtp_credential_created import SmtpCredentialCreated

# TODO update the JSON string below
json = "{}"
# create an instance of SmtpCredentialCreated from a JSON string
smtp_credential_created_instance = SmtpCredentialCreated.from_json(json)
# print the JSON string representation of the object
print(SmtpCredentialCreated.to_json())

# convert the object into a dict
smtp_credential_created_dict = smtp_credential_created_instance.to_dict()
# create an instance of SmtpCredentialCreated from a dict
smtp_credential_created_from_dict = SmtpCredentialCreated.from_dict(smtp_credential_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


