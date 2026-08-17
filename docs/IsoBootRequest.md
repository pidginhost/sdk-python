# IsoBootRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso** | **str** | Catalog ISO slug. Omit it to use the default rescue image. | [optional] 

## Example

```python
from pidginhost_sdk.models.iso_boot_request import IsoBootRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IsoBootRequest from a JSON string
iso_boot_request_instance = IsoBootRequest.from_json(json)
# print the JSON string representation of the object
print(IsoBootRequest.to_json())

# convert the object into a dict
iso_boot_request_dict = iso_boot_request_instance.to_dict()
# create an instance of IsoBootRequest from a dict
iso_boot_request_from_dict = IsoBootRequest.from_dict(iso_boot_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


