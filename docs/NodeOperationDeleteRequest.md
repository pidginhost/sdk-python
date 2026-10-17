# NodeOperationDeleteRequest

A delete additionally requires the hostname typed back.  Checked here rather than in the service on purpose: it is a confirmation that a human typed the right name, which a `source=\"system\"` caller cannot satisfy and must not be asked to. The panel form asks the same question in the same words.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_data_loss_accepted** | **bool** | Acknowledge that data kept on the node itself is destroyed. The drain always deletes emptyDir. | [optional] [default to False]
**confirm_hostname** | **str** | The node&#39;s hostname, typed back exactly. | [optional] [default to '']

## Example

```python
from pidginhost_sdk.models.node_operation_delete_request import NodeOperationDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NodeOperationDeleteRequest from a JSON string
node_operation_delete_request_instance = NodeOperationDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(NodeOperationDeleteRequest.to_json())

# convert the object into a dict
node_operation_delete_request_dict = node_operation_delete_request_instance.to_dict()
# create an instance of NodeOperationDeleteRequest from a dict
node_operation_delete_request_from_dict = NodeOperationDeleteRequest.from_dict(node_operation_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


