# GatewayReenrollRequest

The body of a re-enrollment (spec 8.1 step 6, 13.1): the preview's revision, the networks the gateway routes for and the servers that lose internet while it restarts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revision** | **int** | The gateway&#39;s desired revision from the preview; without it, a preview. | [optional] 
**servers** | **List[int]** | The preview&#39;s server ids. | [optional] 
**networks** | **List[int]** | The preview&#39;s network ids. | [optional] 

## Example

```python
from pidginhost_sdk.models.gateway_reenroll_request import GatewayReenrollRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayReenrollRequest from a JSON string
gateway_reenroll_request_instance = GatewayReenrollRequest.from_json(json)
# print the JSON string representation of the object
print(GatewayReenrollRequest.to_json())

# convert the object into a dict
gateway_reenroll_request_dict = gateway_reenroll_request_instance.to_dict()
# create an instance of GatewayReenrollRequest from a dict
gateway_reenroll_request_from_dict = GatewayReenrollRequest.from_dict(gateway_reenroll_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


