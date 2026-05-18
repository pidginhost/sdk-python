# ConsoleToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 
**ticket** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.console_token import ConsoleToken

# TODO update the JSON string below
json = "{}"
# create an instance of ConsoleToken from a JSON string
console_token_instance = ConsoleToken.from_json(json)
# print the JSON string representation of the object
print(ConsoleToken.to_json())

# convert the object into a dict
console_token_dict = console_token_instance.to_dict()
# create an instance of ConsoleToken from a dict
console_token_from_dict = ConsoleToken.from_dict(console_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


