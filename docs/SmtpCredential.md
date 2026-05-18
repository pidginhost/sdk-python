# SmtpCredential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**label** | **str** |  | [readonly] 
**username** | **str** |  | [readonly] 
**active** | **bool** |  | [readonly] 
**created_at** | **str** |  | [readonly] 
**revoked_at** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.smtp_credential import SmtpCredential

# TODO update the JSON string below
json = "{}"
# create an instance of SmtpCredential from a JSON string
smtp_credential_instance = SmtpCredential.from_json(json)
# print the JSON string representation of the object
print(SmtpCredential.to_json())

# convert the object into a dict
smtp_credential_dict = smtp_credential_instance.to_dict()
# create an instance of SmtpCredential from a dict
smtp_credential_from_dict = SmtpCredential.from_dict(smtp_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


