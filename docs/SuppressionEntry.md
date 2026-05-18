# SuppressionEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**address** | **str** |  | [readonly] 
**reason** | [**ReasonEnum**](ReasonEnum.md) |  | [readonly] 
**detail** | **str** |  | [readonly] 
**created_at** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.suppression_entry import SuppressionEntry

# TODO update the JSON string below
json = "{}"
# create an instance of SuppressionEntry from a JSON string
suppression_entry_instance = SuppressionEntry.from_json(json)
# print the JSON string representation of the object
print(SuppressionEntry.to_json())

# convert the object into a dict
suppression_entry_dict = suppression_entry_instance.to_dict()
# create an instance of SuppressionEntry from a dict
suppression_entry_from_dict = SuppressionEntry.from_dict(suppression_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


