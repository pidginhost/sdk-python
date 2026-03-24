# RDNSUpdateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.rdns_update_response import RDNSUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RDNSUpdateResponse from a JSON string
rdns_update_response_instance = RDNSUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(RDNSUpdateResponse.to_json())

# convert the object into a dict
rdns_update_response_dict = rdns_update_response_instance.to_dict()
# create an instance of RDNSUpdateResponse from a dict
rdns_update_response_from_dict = RDNSUpdateResponse.from_dict(rdns_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


