# ContactsUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_type** | [**ContactTypeEnum**](ContactTypeEnum.md) | Contact type to update  * &#x60;registrant&#x60; - registrant * &#x60;admin&#x60; - admin * &#x60;tech&#x60; - tech * &#x60;billing&#x60; - billing | 
**registrant_id** | **int** | ID of DomainRegistrant to use | 

## Example

```python
from pidginhost_sdk.models.contacts_update import ContactsUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ContactsUpdate from a JSON string
contacts_update_instance = ContactsUpdate.from_json(json)
# print the JSON string representation of the object
print(ContactsUpdate.to_json())

# convert the object into a dict
contacts_update_dict = contacts_update_instance.to_dict()
# create an instance of ContactsUpdate from a dict
contacts_update_from_dict = ContactsUpdate.from_dict(contacts_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


