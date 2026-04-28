# NameserversUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nameservers** | **List[str]** | List of 2-5 nameserver hostnames | 

## Example

```python
from pidginhost_sdk.models.nameservers_update import NameserversUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of NameserversUpdate from a JSON string
nameservers_update_instance = NameserversUpdate.from_json(json)
# print the JSON string representation of the object
print(NameserversUpdate.to_json())

# convert the object into a dict
nameservers_update_dict = nameservers_update_instance.to_dict()
# create an instance of NameserversUpdate from a dict
nameservers_update_from_dict = NameserversUpdate.from_dict(nameservers_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


