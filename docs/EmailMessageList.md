# EmailMessageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[EmailMessageSummary]**](EmailMessageSummary.md) |  | 
**count** | **int** |  | 
**page** | **int** |  | 
**per_page** | **int** |  | 

## Example

```python
from pidginhost_sdk.models.email_message_list import EmailMessageList

# TODO update the JSON string below
json = "{}"
# create an instance of EmailMessageList from a JSON string
email_message_list_instance = EmailMessageList.from_json(json)
# print the JSON string representation of the object
print(EmailMessageList.to_json())

# convert the object into a dict
email_message_list_dict = email_message_list_instance.to_dict()
# create an instance of EmailMessageList from a dict
email_message_list_from_dict = EmailMessageList.from_dict(email_message_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


