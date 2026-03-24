# ServerUsageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**uptime** | **int** |  | 
**uptime_text** | **str** |  | 
**cpu** | **Dict[str, object]** |  | 
**memory** | **Dict[str, object]** |  | 

## Example

```python
from pidginhost_sdk.models.server_usage_response import ServerUsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServerUsageResponse from a JSON string
server_usage_response_instance = ServerUsageResponse.from_json(json)
# print the JSON string representation of the object
print(ServerUsageResponse.to_json())

# convert the object into a dict
server_usage_response_dict = server_usage_response_instance.to_dict()
# create an instance of ServerUsageResponse from a dict
server_usage_response_from_dict = ServerUsageResponse.from_dict(server_usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


