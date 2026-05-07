# ActivityLogEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**var_date** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.activity_log_entry import ActivityLogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityLogEntry from a JSON string
activity_log_entry_instance = ActivityLogEntry.from_json(json)
# print the JSON string representation of the object
print(ActivityLogEntry.to_json())

# convert the object into a dict
activity_log_entry_dict = activity_log_entry_instance.to_dict()
# create an instance of ActivityLogEntry from a dict
activity_log_entry_from_dict = ActivityLogEntry.from_dict(activity_log_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


