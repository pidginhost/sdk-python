# TLDCatalog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tlds** | [**List[TLD]**](TLD.md) |  | 
**default_nameservers** | **str** |  | 
**currency** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.tld_catalog import TLDCatalog

# TODO update the JSON string below
json = "{}"
# create an instance of TLDCatalog from a JSON string
tld_catalog_instance = TLDCatalog.from_json(json)
# print the JSON string representation of the object
print(TLDCatalog.to_json())

# convert the object into a dict
tld_catalog_dict = tld_catalog_instance.to_dict()
# create an instance of TLDCatalog from a dict
tld_catalog_from_dict = TLDCatalog.from_dict(tld_catalog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


