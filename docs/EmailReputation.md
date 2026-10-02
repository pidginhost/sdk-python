# EmailReputation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bounce_rate_pct** | **str** |  | 
**complaint_rate_pct** | **str** |  | 
**msgs_sent_24h** | **int** |  | 
**msgs_sent_30d** | **int** |  | 

## Example

```python
from pidginhost_sdk.models.email_reputation import EmailReputation

# TODO update the JSON string below
json = "{}"
# create an instance of EmailReputation from a JSON string
email_reputation_instance = EmailReputation.from_json(json)
# print the JSON string representation of the object
print(EmailReputation.to_json())

# convert the object into a dict
email_reputation_dict = email_reputation_instance.to_dict()
# create an instance of EmailReputation from a dict
email_reputation_from_dict = EmailReputation.from_dict(email_reputation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


