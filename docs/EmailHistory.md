# EmailHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**subject** | **str** |  | [readonly] 
**var_date** | **str** |  | [readonly] 
**address** | **str** |  | [readonly] 
**read** | **bool** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.email_history import EmailHistory

# TODO update the JSON string below
json = "{}"
# create an instance of EmailHistory from a JSON string
email_history_instance = EmailHistory.from_json(json)
# print the JSON string representation of the object
print(EmailHistory.to_json())

# convert the object into a dict
email_history_dict = email_history_instance.to_dict()
# create an instance of EmailHistory from a dict
email_history_from_dict = EmailHistory.from_dict(email_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


