# ActivityLogResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | [**List[ActivityLogEntry]**](ActivityLogEntry.md) |  | 

## Example

```python
from pidginhost_sdk.models.activity_log_response import ActivityLogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityLogResponse from a JSON string
activity_log_response_instance = ActivityLogResponse.from_json(json)
# print the JSON string representation of the object
print(ActivityLogResponse.to_json())

# convert the object into a dict
activity_log_response_dict = activity_log_response_instance.to_dict()
# create an instance of ActivityLogResponse from a dict
activity_log_response_from_dict = ActivityLogResponse.from_dict(activity_log_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


