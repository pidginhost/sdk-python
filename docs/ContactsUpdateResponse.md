# ContactsUpdateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.contacts_update_response import ContactsUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContactsUpdateResponse from a JSON string
contacts_update_response_instance = ContactsUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(ContactsUpdateResponse.to_json())

# convert the object into a dict
contacts_update_response_dict = contacts_update_response_instance.to_dict()
# create an instance of ContactsUpdateResponse from a dict
contacts_update_response_from_dict = ContactsUpdateResponse.from_dict(contacts_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


