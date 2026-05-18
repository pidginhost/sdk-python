# NameserversUpdateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.nameservers_update_response import NameserversUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NameserversUpdateResponse from a JSON string
nameservers_update_response_instance = NameserversUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(NameserversUpdateResponse.to_json())

# convert the object into a dict
nameservers_update_response_dict = nameservers_update_response_instance.to_dict()
# create an instance of NameserversUpdateResponse from a dict
nameservers_update_response_from_dict = NameserversUpdateResponse.from_dict(nameservers_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


