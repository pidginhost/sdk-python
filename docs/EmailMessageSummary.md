# EmailMessageSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** |  | 
**status** | **str** |  | 
**last_event_at** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.email_message_summary import EmailMessageSummary

# TODO update the JSON string below
json = "{}"
# create an instance of EmailMessageSummary from a JSON string
email_message_summary_instance = EmailMessageSummary.from_json(json)
# print the JSON string representation of the object
print(EmailMessageSummary.to_json())

# convert the object into a dict
email_message_summary_dict = email_message_summary_instance.to_dict()
# create an instance of EmailMessageSummary from a dict
email_message_summary_from_dict = EmailMessageSummary.from_dict(email_message_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


