# StatsDay


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
**day** | **date** |  | 

## Example

```python
from pidginhost_sdk.models.stats_day import StatsDay

# TODO update the JSON string below
json = "{}"
# create an instance of StatsDay from a JSON string
stats_day_instance = StatsDay.from_json(json)
# print the JSON string representation of the object
print(StatsDay.to_json())

# convert the object into a dict
stats_day_dict = stats_day_instance.to_dict()
# create an instance of StatsDay from a dict
stats_day_from_dict = StatsDay.from_dict(stats_day_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


