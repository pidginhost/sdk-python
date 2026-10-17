# DashboardServer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**hostname** | **str** |  | 
**status** | **str** |  | 
**project** | **str** |  | 
**cpus** | **int** |  | 
**memory** | **int** |  | 

## Example

```python
from pidginhost_sdk.models.dashboard_server import DashboardServer

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardServer from a JSON string
dashboard_server_instance = DashboardServer.from_json(json)
# print the JSON string representation of the object
print(DashboardServer.to_json())

# convert the object into a dict
dashboard_server_dict = dashboard_server_instance.to_dict()
# create an instance of DashboardServer from a dict
dashboard_server_from_dict = DashboardServer.from_dict(dashboard_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


