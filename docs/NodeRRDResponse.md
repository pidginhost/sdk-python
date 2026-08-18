# NodeRRDResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[object]** |  | 
**timeframe** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.node_rrd_response import NodeRRDResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NodeRRDResponse from a JSON string
node_rrd_response_instance = NodeRRDResponse.from_json(json)
# print the JSON string representation of the object
print(NodeRRDResponse.to_json())

# convert the object into a dict
node_rrd_response_dict = node_rrd_response_instance.to_dict()
# create an instance of NodeRRDResponse from a dict
node_rrd_response_from_dict = NodeRRDResponse.from_dict(node_rrd_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


