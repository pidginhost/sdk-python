# ServerUpgradeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upgrading** | **bool** |  | 

## Example

```python
from pidginhost_sdk.models.server_upgrade_response import ServerUpgradeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServerUpgradeResponse from a JSON string
server_upgrade_response_instance = ServerUpgradeResponse.from_json(json)
# print the JSON string representation of the object
print(ServerUpgradeResponse.to_json())

# convert the object into a dict
server_upgrade_response_dict = server_upgrade_response_instance.to_dict()
# create an instance of ServerUpgradeResponse from a dict
server_upgrade_response_from_dict = ServerUpgradeResponse.from_dict(server_upgrade_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


