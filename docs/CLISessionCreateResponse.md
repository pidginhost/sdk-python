# CLISessionCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **UUID** |  | 
**verification_url** | **str** |  | 
**expires_at** | **str** |  | 
**poll_interval** | **int** | Recommended polling interval in seconds | 

## Example

```python
from pidginhost_sdk.models.cli_session_create_response import CLISessionCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CLISessionCreateResponse from a JSON string
cli_session_create_response_instance = CLISessionCreateResponse.from_json(json)
# print the JSON string representation of the object
print(CLISessionCreateResponse.to_json())

# convert the object into a dict
cli_session_create_response_dict = cli_session_create_response_instance.to_dict()
# create an instance of CLISessionCreateResponse from a dict
cli_session_create_response_from_dict = CLISessionCreateResponse.from_dict(cli_session_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


