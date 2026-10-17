# TLD


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**tld** | **str** |  | 
**price** | **decimal.Decimal** | Euro without TVA | 
**renew_price** | **decimal.Decimal** | Euro without TVA | [optional] 
**transfer_price** | **decimal.Decimal** | Euro without TVA | [optional] 
**registrar** | **str** |  | 
**api_renewable** | **bool** |  | [optional] 
**idna_support** | **bool** |  | [optional] 
**wg_support** | **bool** |  | [optional] 
**reactivate_max_days** | **int** |  | [optional] 
**min_years** | **int** | Smallest registration term the registry accepts (e.g. 2 for .ai). | [optional] 
**year_step** | **int** | Allowed step between registration terms (e.g. 2 for .ai → 2, 4, 6 years). | [optional] 

## Example

```python
from pidginhost_sdk.models.tld import TLD

# TODO update the JSON string below
json = "{}"
# create an instance of TLD from a JSON string
tld_instance = TLD.from_json(json)
# print the JSON string representation of the object
print(TLD.to_json())

# convert the object into a dict
tld_dict = tld_instance.to_dict()
# create an instance of TLD from a dict
tld_from_dict = TLD.from_dict(tld_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


