# ServerProductUpgradeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package** | **str** | ID or slug | 

## Example

```python
from pidginhost_sdk.models.server_product_upgrade_request import ServerProductUpgradeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServerProductUpgradeRequest from a JSON string
server_product_upgrade_request_instance = ServerProductUpgradeRequest.from_json(json)
# print the JSON string representation of the object
print(ServerProductUpgradeRequest.to_json())

# convert the object into a dict
server_product_upgrade_request_dict = server_product_upgrade_request_instance.to_dict()
# create an instance of ServerProductUpgradeRequest from a dict
server_product_upgrade_request_from_dict = ServerProductUpgradeRequest.from_dict(server_product_upgrade_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


