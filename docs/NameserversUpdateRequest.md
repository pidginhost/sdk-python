# NameserversUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nameservers** | **List[str]** | List of 2-5 nameserver hostnames | 

## Example

```python
from pidginhost_sdk.models.nameservers_update_request import NameserversUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NameserversUpdateRequest from a JSON string
nameservers_update_request_instance = NameserversUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(NameserversUpdateRequest.to_json())

# convert the object into a dict
nameservers_update_request_dict = nameservers_update_request_instance.to_dict()
# create an instance of NameserversUpdateRequest from a dict
nameservers_update_request_from_dict = NameserversUpdateRequest.from_dict(nameservers_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


