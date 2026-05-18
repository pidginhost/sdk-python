# CLISessionPollResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**CLISessionPollResponseStatusEnum**](CLISessionPollResponseStatusEnum.md) |  | 
**token_key** | **str** | Only present when status is approved | [optional] 
**token_name** | **str** |  | [optional] 
**token_scope** | **str** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.cli_session_poll_response import CLISessionPollResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CLISessionPollResponse from a JSON string
cli_session_poll_response_instance = CLISessionPollResponse.from_json(json)
# print the JSON string representation of the object
print(CLISessionPollResponse.to_json())

# convert the object into a dict
cli_session_poll_response_dict = cli_session_poll_response_instance.to_dict()
# create an instance of CLISessionPollResponse from a dict
cli_session_poll_response_from_dict = CLISessionPollResponse.from_dict(cli_session_poll_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


