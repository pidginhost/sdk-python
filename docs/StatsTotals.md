# StatsTotals


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sent** | **int** |  | 
**delivered** | **int** |  | 
**hard_bounce** | **int** |  | 
**soft_bounce** | **int** |  | 
**complaint** | **int** |  | 
**opened** | **int** |  | 
**clicked** | **int** |  | 
**rejected** | **int** |  | 

## Example

```python
from pidginhost_sdk.models.stats_totals import StatsTotals

# TODO update the JSON string below
json = "{}"
# create an instance of StatsTotals from a JSON string
stats_totals_instance = StatsTotals.from_json(json)
# print the JSON string representation of the object
print(StatsTotals.to_json())

# convert the object into a dict
stats_totals_dict = stats_totals_instance.to_dict()
# create an instance of StatsTotals from a dict
stats_totals_from_dict = StatsTotals.from_dict(stats_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


