# DashboardResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_count** | **int** |  | 
**hosting_count** | **int** |  | 
**servers** | [**List[DashboardServer]**](DashboardServer.md) |  | 
**hosting** | [**List[HostingService]**](HostingService.md) |  | 
**expiring_domains** | [**List[ExpiringDomain]**](ExpiringDomain.md) |  | 

## Example

```python
from pidginhost_sdk.models.dashboard_resources import DashboardResources

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardResources from a JSON string
dashboard_resources_instance = DashboardResources.from_json(json)
# print the JSON string representation of the object
print(DashboardResources.to_json())

# convert the object into a dict
dashboard_resources_dict = dashboard_resources_instance.to_dict()
# create an instance of DashboardResources from a dict
dashboard_resources_from_dict = DashboardResources.from_dict(dashboard_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


