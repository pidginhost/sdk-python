# ServerMonitoringRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Email the account when this server stops unexpectedly or its host stops responding. Free. | 

## Example

```python
from pidginhost_sdk.models.server_monitoring_request import ServerMonitoringRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServerMonitoringRequest from a JSON string
server_monitoring_request_instance = ServerMonitoringRequest.from_json(json)
# print the JSON string representation of the object
print(ServerMonitoringRequest.to_json())

# convert the object into a dict
server_monitoring_request_dict = server_monitoring_request_instance.to_dict()
# create an instance of ServerMonitoringRequest from a dict
server_monitoring_request_from_dict = ServerMonitoringRequest.from_dict(server_monitoring_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


