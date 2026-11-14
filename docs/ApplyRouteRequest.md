# ApplyRouteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**servers** | **List[int]** | The servers to re-render and reboot; each one listed reboots. | 

## Example

```python
from pidginhost_sdk.models.apply_route_request import ApplyRouteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyRouteRequest from a JSON string
apply_route_request_instance = ApplyRouteRequest.from_json(json)
# print the JSON string representation of the object
print(ApplyRouteRequest.to_json())

# convert the object into a dict
apply_route_request_dict = apply_route_request_instance.to_dict()
# create an instance of ApplyRouteRequest from a dict
apply_route_request_from_dict = ApplyRouteRequest.from_dict(apply_route_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


